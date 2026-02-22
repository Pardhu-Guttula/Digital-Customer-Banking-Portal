variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "location" {
  description = "The Azure region"
  type        = string
}

variable "app_service_name" {
  description = "The name of the App Service"
  type        = string
}

variable "app_service_plan_name" {
  description = "The name of the App Service Plan"
  type        = string
}

variable "api_management_name" {
  description = "The name of the API Management Instance"
  type        = string
}

variable "publisher_name" {
  description = "The publisher name for the API Management Instance"
  type        = string
}

variable "publisher_email" {
  description = "The publisher email for the API Management Instance"
  type        = string
}

variable "sql_server_name" {
  description = "The name of the SQL Server"
  type        = string
}

variable "sql_admin_login" {
  description = "The admin username for the SQL Server"
  type        = string
}

variable "sql_admin_password" {
  description = "The admin password for the SQL Server"
  type        = string
  sensitive   = true
}

variable "sql_database_name" {
  description = "The name of the SQL Database"
  type        = string
}

variable "storage_account_name" {
  description = "The name of the Storage Account"
  type        = string
}

variable "aad_domain_name" {
  description = "The domain name for Azure AD Domain Services"
  type        = string
}

variable "aad_domain_password" {
  description = "The password for the Azure AD Domain Services administrator"
  type        = string
  sensitive   = true
}

variable "key_vault_name" {
  description = "The name of the Key Vault"
  type        = string
}