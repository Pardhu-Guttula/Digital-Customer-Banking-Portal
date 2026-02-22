terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
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

resource "azurerm_app_service" "example" {
  name                = "example-appservice"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
}

resource "azurerm_frontdoor" "example" {
  name                = "example-frontdoor"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  routing_rule {
    name               = "example-routingrule"
    accepted_protocols = ["Https"]
    patterns_to_match  = ["/*"]
    frontend_endpoints = [azurerm_frontdoor_frontend_endpoint.example.name]
    forwarding_configuration {
      forwarding_protocol        = "HttpsOnly"
      backend_pool               = azurerm_frontdoor_backend_pool.example.name
      cache_use_dynamic_compression = true
      cache_query_parameter_strip_directive = "StripAllExcept"
    }
  }
}

resource "azurerm_frontdoor_frontend_endpoint" "example" {
  name                = "example-frontendendpoint"
  resource_group_name = azurerm_resource_group.example.name
  frontdoor_name      = azurerm_frontdoor.example.name
  host_name           = azurerm_frontdoor.example.host_name
}

resource "azurerm_frontdoor_backend_pool" "example" {
  name                = "example-backendpool"
  resource_group_name = azurerm_resource_group.example.name
  frontdoor_name      = azurerm_frontdoor.example.name
  backend {
    host_header       = azurerm_app_service.example.default_site_hostname
    address           = azurerm_app_service.example.default_site_hostname
    http_port         = 80
    https_port        = 443
  }
}

resource "azurerm_api_management" "example" {
  name                = "example-apim"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  publisher_name      = "Example Publisher"
  publisher_email     = "publisher@example.com"
  sku_name            = "Developer_1"
}

resource "azurerm_api_management_api" "example" {
  name                = "example-api"
  resource_group_name = azurerm_resource_group.example.name
  api_management_name = azurerm_api_management.example.name
  revision            = "1"
  display_name        = "Example API"
  path                = "example"
  protocols           = ["https"]
}
