variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "example-resources"
}

variable "location" {
  description = "The Azure region"
  type        = string
  default     = "West Europe"
}

variable "sql_admin_password" {
  description = "The password for the SQL server admin user"
  type        = string
}
