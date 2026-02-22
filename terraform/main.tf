provider "azurerm" {
  features {}
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-self-service-portal"
  location = "East US"
}

resource "azurerm_app_service_plan" "app_service_plan" {
  name                = "appservice-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "web_app" {
  name                = "self-service-web-app"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.app_service_plan.id
  site_config {
    always_on                = true
    managed_pipeline_mode    = "Integrated"
    ftps_state               = "FtpsOnly"
  }
}

resource "azurerm_storage_account" "storage" {
  name                     = "storageselfservice"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_key_vault" "key_vault" {
  name                = "selfservice-keyvault"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku_name            = "standard"
}

resource "azurerm_log_analytics_workspace" "log_analytics" {
  name                = "log-self-service"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
}

resource "azurerm_monitor_diagnostic_setting" "diag" {
  name                       = "diag-self-service"
  target_resource_id         = azurerm_app_service.web_app.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.log_analytics.id
  enabled_log {
    category = "AppServiceHTTPLogs"
    enabled  = true
  }
  metric {
    category = "AllMetrics"
    enabled  = true
  }
}

resource "azurerm_azuread_b2c_directory" "b2c" {
  name     = "selfservice-b2c"
  location = azurerm_resource_group.rg.location
}

resource "azurerm_function_app" "function_app" {
  name                       = "selfservice-functionapp"
  location                   = azurerm_resource_group.rg.location
  resource_group_name        = azurerm_resource_group.rg.name
  app_service_plan_id        = azurerm_app_service_plan.app_service_plan.id
  storage_account_name       = azurerm_storage_account.storage.name
  storage_account_access_key = azurerm_storage_account.storage.primary_access_key
}

resource "azurerm_logic_app" "self_service_workflow" {
  name                = "self-service-workflow"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}
