.. title:: Nutanix Move

.. toctree:: 
   :maxdepth: 2
   :caption: Nutanix Move Lab
   :name: _move
   :hidden:

   move/preparation
   move/move_deployment
   move/login_move
   move/source_environment
   move/target_environment
   move/create_mp
   move/test_mp
   move/cutover
   move/download_file


.. _getting_started:

###############
Getting Started
###############

Welcome to Nutanix Move's Hands-on Lab!

Nutanix Move (Move) is a cross-hypervisor mobility solution to move VMs with minimal downtime. Move supports migration from the following sources to targets, where first platform being the source and second platform being the target.

What's New
==========

- Workshop updated for the following software versions:
   - AOS 5.20.x
   - PC 2022.x
   - Move 4.5.1

Agenda
======
   - Preparation
   - Move Deployment
   - Add Source Environment
   - Add Target Environment
   - Creating Migration Plan

Environment Details
===================

Each attendees will be assigned a Remote lab for information please see or download `Lab Access Information <https://www.dropbox.com/s/sxzr5t4au9f8483/Move%20Lab%20Access%20Information.xlsx?dl=1>`_ document.

Lab Access Methods
==================

Please only use credentials provided in above document.

VPN option: Pulse Secure VPN Client
-----------------------------------

1. If client already installed skip to step 5
2. To download the client, login to https://blr-vpn.xlabs.nutanix.com or https://phx-vpn.xlabs.nutanix.com using the supplied user credentials
    Or
 
  - Direct Download:
     - `Windows 32 bit <https://noc.rmutp.ac.th/wp-content/uploads/32bitinstaller.msi>`_
     - `Windows 64 bit <https://noc.rmutp.ac.th/wp-content/uploads/64bitinstaller.msi>`_
     - `Mac OS <https://noc.rmutp.ac.th/wp-content/uploads/macinstaller.dmg>`_

3. Download and install client
4. Logout of the Web UI
5. Open client and **ADD** a connection with the following details:

   Use BLR:

   - **Type:** Policy Secure (UAC) or Connection Server(VPN)
   - **Name:** X-Labs - BLR
   - **Server URL:** blr-vpn.xlabs.nutanix.com
   
   Or PHX:

   - **Type** - Policy Secure (UAC) or Connection Server(VPN)
   - **Name** - X-Labs - PHX
   - **Server URL** - phx-vpn.xlabs.nutanix.com

6. Once setup, login with the supplied credentials

**Incase can't install Pulse VPN Client**

Parallels VDI
-------------
1. Login to https://blr-ras.xlabs.nutanix.com or https://phx-ras.xlabs.nutanix.com using your supplied credentials
2. Select HTML5 (web browser) OR Install the Parallels Client
3. Select a desktop or application of your choice.

Frame VDI
---------
1. Login to https://console.nutanix.com/x/labs using your supplied credentials
2. Select the most applicable datacenter launchpad for the clusters you will be accessing or modify an existing selection using the breadcrumb menu at the top-center of the page
3. Launch desktop


Cluster Credentials
-------------------

.. note::

  The *<Cluster Password>* is unique to each cluster and will be provided by `Lab Access Information <https://www.dropbox.com/s/sxzr5t4au9f8483/Move%20Lab%20Access%20Information.xlsx?dl=1>`_ document of the Workshop.

.. list-table::
  :widths: 35 32 32
  :header-rows: 1

  * - Credential
    - Username
    - Password
  * - Prism Element
    - admin
    - *<Cluster Password>*
  * - Prism Central
    - admin
    - *<Cluster Password>*
  * - Controller VM
    - nutanix
    - *<Cluster Password>*
  * - Prism Central VM
    - nutanix
    - *<Cluster Password>*