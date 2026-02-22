variable "resource_group_location" {
  description = "The location of the resource group."
  type        = string
  default     = "East US"
}

variable "app_service_plan_name" {
  description = "The name of the App Service Plan."
  type        = string
  default     = "appservice-plan"
}

variable "web_app_name" {
  description = "The name of the Web App."
  type        = string
  default     = "self-service-web-app"
}

variable "storage_account_name" {
  description = "The name of the Storage Account."
  type        = string
  default     = "storageselfservice"
}

variable "key_vault_name" {
  description = "The name of the Key Vault."
  type        = string
  default     = "selfservice-keyvault"
}

variable "log_analytics_workspace_name" {
  description = "The name of the Log Analytics Workspace."
  type        = string
  default     = "log-self-service"
}

variable "b2c_directory_name" {
  description = "The name of the Azure AD B2C Directory."
  type        = string
  default     = "selfservice-b2c"
}

variable "function_app_name" {
  description = "The name of the Function App."
  type        = string
  default     = "selfservice-functionapp"
}

variable "logic_app_name" {
  description = "The name of the Logic App."
  type        = string
  default     = "self-service-workflow"
}
