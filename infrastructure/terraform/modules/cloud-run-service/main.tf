resource "google_cloud_run_v2_service" "this" {
  project             = var.project_id
  location            = var.region
  name                = var.name
  deletion_protection = true

  template {
    service_account = var.service_account_email
    scaling {
      min_instance_count = 0
      max_instance_count = var.max_instances
    }
    containers {
      image = var.image_digest
      ports { container_port = 8080 }
      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
        cpu_idle = true
      }
      startup_probe {
        http_get {
          path = "/health/live"
          port = 8080
        }
      }
      liveness_probe {
        http_get {
          path = "/health/live"
          port = 8080
        }
      }
    }
    max_instance_request_concurrency = 40
    timeout                          = "30s"
  }
  ingress = "INGRESS_TRAFFIC_ALL"
}
