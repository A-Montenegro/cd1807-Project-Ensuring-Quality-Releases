resource "azurerm_network_interface" "" {
  name                = "network_interface_1"
  location            = "eastus"
  resource_group_name = "resource_group_1"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = ""
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = ""
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = "linux-test"
  location            = "eastus"
  resource_group_name = "resource_group_1"
  size                = "Standard_DS2_v2"
  admin_username      = "alber"
  network_interface_ids = []
  admin_ssh_key {
    username   = "alber"
    public_key = "file("~/.ssh/id_rsa.pub")"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
