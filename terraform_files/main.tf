terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.16.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "jenkins" {
  name = "jenkins/jenkins:lts-jdk11"
}

resource "docker_container" "jenkins" {
  image = docker_image.jenkins.latest
  name  = "jenkins_container"
  ports {
    internal = 8080
    external = 8080
  }
}