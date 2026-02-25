provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageaccount"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_static_site" "example" {
  name                = "examplestaticwebsite"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku_tier            = "Free"

  provider_b2c  = "aadB2C"
  custom_domain = "example.com"
}

resource "azurerm_cdn_profile" "example" {
  name                = "exampleCdnProfile"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku {
    name = "Standard_Microsoft"
  }
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-resources"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "example" {
  name                = "example-app"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
}

resource "azurerm_api_management" "example" {
  name                = "exampleAPI"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  publisher_name      = "ExamplePublisher"
  publisher_email     = "example@example.com"
  sku_name            = "Developer_1"
}

resource "azurerm_sql_server" "example" {
  name                = "mysqlserver"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  version             = "12.0"
  administrator_login = "sqladmin"
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_sql_database" "example" {
  name                = "mydatabase"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  server_name         = azurerm_sql_server.example.name
  edition             = "Basic"
}

resource "azurerm_cosmosdb_account" "example" {
  name                = "cosmosdbaccount"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  consistency_policy {
    consistency_level = "BoundedStaleness"
    max_interval_in_seconds = 10
    max_staleness_prefix = 200
  }
  geo_location {
    location = azurerm_resource_group.example.location
    failover_priority = 0
  }
}
