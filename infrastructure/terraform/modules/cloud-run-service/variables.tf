variable "project_id" { type = string }
variable "region" { type = string }
variable "name" { type = string }
variable "image_digest" {
  type = string
  validation {
    condition     = can(regex("@sha256:[a-f0-9]{64}$", var.image_digest))
    error_message = "Use an immutable sha256 image digest."
  }
}
variable "service_account_email" { type = string }
variable "max_instances" {
  type    = number
  default = 3
}
