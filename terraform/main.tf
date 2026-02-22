provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_front_door" "example" {
  name                = "example-frontdoor"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
}

resource "azurerm_app_service" "web_app" {
  name                = "example-webapp"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
  site_config {
    always_on = true
  }
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-appserviceplan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_static_site" "example" {
  name                = "example-staticwebapp"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_sql_database" "example" {
  name                = "example-sqldb"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  server_name         = azurerm_sql_server.example.name
}

resource "azurerm_sql_server" "example" {
  name                         = "example-sqlserver"
  resource_group_name          = azurerm_resource_group.example.name
  location                     = azurerm_resource_group.example.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_username
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_cosmosdb_account" "example" {
  name                = "example-cosmosdb"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  consistency_policy {
    consistency_level = "Session"
  }
}

resource "azurerm_signalr_service" "example" {
  name                = "example-signalr"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    name     = "Free_F1"
    capacity = 1
  }
}

resource "azurerm_notification_hub" "example" {
  name                = "example-notificationhub"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  notification_hub_namespace = azurerm_notification_hub_namespace.example.name
}

resource "azurerm_notification_hub_namespace" "example" {
  name                = "example-notificationnamespace"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku_name            = "Free"
}

resource "azurerm_key_vault" "example" {
  name                = "example-keyvault"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  tenant_id           = var.tenant_id
  sku_name            = "standard"
}

resource "azurerm_monitor_diagnostic_setting" "example" {
  name               = "example-diagnostics"
  target_resource_id = azurerm_web_app_service.example.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.example.id
  enabled_log {
    category = "AppServiceHTTPLogs"
    enabled  = true
  }
  metric {
    category = "AllMetrics"
    enabled  = true
  }
}

resource "azurerm_log_analytics_workspace" "example" {
  name                = "example-logs"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_active_directory_domain_service" "example" {
  name                = "example-adds"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  domain_name         = var.domain_name
  sku_name            = "standard"
}

resource "azurerm_devops_project" "example" {
  name                = "example-devops-project"
  organization        = var.organization_name
  azdo_pat            = var.azdo_pat
}

resource "azurerm_monitor_autoscale_setting" "example" {
  name                = "example-autoscale"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  target_resource_id  = azurerm_app_service.example.id
  profile {
    name = "defaultProfile"
    capacity {
      default = 1
      minimum = 1
      maximum = 10
    }
    rule {
      metric_trigger {
        metric_name    = "CpuPercentage"
        metric_resource_id = azurerm_app_service.example.id
        operator       = "GreaterThan"
        statistic      = "Average"
        threshold      = 75
        time_aggregation   = "Average"
        time_grain      = "PT1M"
        time_window     = "PT5M"
      }
      scale_action {
        direction = "Increase"
        type      = "ChangeCount"
        value     = 1
        cooldown  = "PT5M"
      }
    }
    rule {
      metric_trigger {
        metric_name    = "CpuPercentage"
        metric_resource_id = azurerm_app_service.example.id
        operator       = "LessThan"
        statistic      = "Average"
        threshold      = 25
        time_aggregation   = "Average"
        time_grain      = "PT1M"
        time_window     = "PT5M"
      }
      scale_action {
        direction = "Decrease"
        type      = "ChangeCount"
        value     = 1
        cooldown  = "PT5M"
      }
    }
  }
}
