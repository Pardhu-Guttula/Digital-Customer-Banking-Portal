variable "sql_admin_username" {
  description = "The administrator username for SQL Server"
  type        = string
}

variable "sql_admin_password" {
  description = "The administrator password for SQL Server"
  type        = string
  sensitive   = true
}

variable "tenant_id" {
  description = "The Tenant ID for Azure Active Directory"
  type        = string
}

variable "domain_name" {
  description = "The domain name for Active Directory Domain Service"
  type        = string
}

variable "organization_name" {
  description = "The organization name for Azure DevOps"
  type        = string
}

variable "azdo_pat" {
  description = "The Personal Access Token for Azure DevOps"
  type        = string
  sensitive   = true
}
