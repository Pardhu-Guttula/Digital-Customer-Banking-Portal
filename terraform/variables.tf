variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "example-resources"
}

variable "location" {
  description = "The Azure location where resources will be deployed"
  type        = string
  default     = "East US"
}

variable "app_service_name" {
  description = "The name of the App Service"
  type        = string
}

variable "static_site_name" {
  description = "The name of the Static Site"
  type        = string
}

variable "function_app_name" {
  description = "The name of the Function App"
  type        = string
}

variable "logic_app_name" {
  description = "The name of the Logic App"
  type        = string
}
