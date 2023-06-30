provider "azurerm" {
  tenant_id       = "637c6471-612c-465d-af0b-7ae255d7dc68"
  subscription_id = "e80f7f84-f877-4140-9ea9-b2c7d113e3d1"
  client_id       = "d00ae108-0fe5-468d-9c61-8ee59c096ec8"
  client_secret   = "HlW8Q~Zfzzl6ZPSut3SUOoIZTdgWFJvQNx4MociR"
  features {}
}
terraform {
  backend "azurerm" {
    storage_account_name = "tfstate180983178"
    container_name       = "tfstate"
    key                  = "test.terraform.tfstate"
    access_key           = "4Y3uSMMsWPII1iSfydaLhhUhI4bMnEORtvU0OGphtvqjyFWHMI+srt4Kird8cvxNnnMdqZFv+zcm+AStk1a2Sg=="
  }
}
module "resource_group" {
  source               = "../../modules/resource_group"
  resource_group       = "${var.resource_group}"
  location             = "${var.location}"
}
module "network" {
  source               = "../../modules/network"
  address_space        = "${var.address_space}"
  location             = "${var.location}"
  virtual_network_name = "${var.virtual_network_name}"
  application_type     = "${var.application_type}"
  resource_type        = "NET"
  resource_group       = "${module.resource_group.resource_group_name}"
  address_prefix_test  = "${var.address_prefix_test}"
}

module "nsg-test" {
  source           = "../../modules/networksecuritygroup"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "NSG"
  resource_group   = "${module.resource_group.resource_group_name}"
  subnet_id        = "${module.network.subnet_id_test}"
  address_prefix_test = "${var.address_prefix_test}"
}
module "appservice" {
  source           = "../../modules/appservice"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "AppService"
  resource_group   = "${module.resource_group.resource_group_name}"
}
module "publicip" {
  source           = "../../modules/publicip"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "publicip"
  resource_group   = "${module.resource_group.resource_group_name}"
}