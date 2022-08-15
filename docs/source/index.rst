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

Each attendees will be assigned a Remote lab for information please see or download `Lab Access Information <https://docs.google.com/spreadsheets/d/1LOzz8wt8srnTq--ip-h6NtNLryxfrxrltOEE5_y5RDI/edit?usp=sharing>`_ document.

Lab Access Methods
==================

Please only use credentials provided in above document.

VPN option: Pulse Secure VPN Client
-----------------------------------

1. If client already installed skip to step 5
2. To download the client, login to https://xlv-uswest1.nutanix.com or https://xlv-blr.xlabs.nutanix.com using the supplied user credentials
    Or
  - Direct Download:
     - `Windows 32 bit <https://noc.rmutp.ac.th/wp-content/uploads/32bitinstaller.msi>`_
     - `Windows 64 bit <https://noc.rmutp.ac.th/wp-content/uploads/64bitinstaller.msi>`_
     - `Mac OS <https://noc.rmutp.ac.th/wp-content/uploads/macinstaller.dmg>`_
3. Download and install client
4. Logout of the Web UI
5. Open client and **ADD** a connection with the following details:

   Use BLR:

   - **Type:** Policy Secure (UAC) or Connection Server(VPN)\
   - **Name:** X-Labs - BLR
   - **Server URL:** xlv-blr.xlabs.nutanix.com\
   
   Or PHX:

   - **Type** - Policy Secure (UAC) or Connection Server
   - **Name** - X-Labs - PHX
   - **Server URL** - xlv-uswest1.nutanix.com

6. Once setup, login with the supplied credentials

Cluster Credentials
-------------------

.. note::

  The *<Cluster Password>* is unique to each cluster and will be provided by `Lab Access Information <https://docs.google.com/spreadsheets/d/1LOzz8wt8srnTq--ip-h6NtNLryxfrxrltOEE5_y5RDI/edit?usp=sharing>`_ document of the Workshop.

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