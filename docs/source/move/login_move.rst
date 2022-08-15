.. _login_move:

Logging in to Move UI
*********************

Before you begin
^^^^^^^^^^^^^^^^

For static IP deployment, ensure to assign static IP address to Move.
Note: For information on assigning static IP address to Move, refer to Assigning a Static IP Address to Move.

About this task
^^^^^^^^^^^^^^^

To log on to Move UI, do the following:

Procedure
^^^^^^^^^

1. Open a web browser, enter the FQDN or IP address of the VM.
2. (First-time log on only) If you are logging in for the first time, do the following:
     - Click the **I have read and agree to terms and conditions** option, and then click **Continue**.
     - In the Nutanix Customer Experience Program screen, click **OK**.
      .. note::
         By participating in the Nutanix Customer Experience Program, Nutanix collects non-identifying information for product improvement. Information such as type of source and target, number of migrated VMs, Move version, operating system type of migrated VMs.
         You can opt out of Nutanix Customer Experience Program from the Move dashboard after logging in. Click the gear icon on the top-right corner, then click **Experience Improvement**. Uncheck the **Participate** check box.
     - In the logon screen, set a password for the nutanix user in the **Enter new password** and **Re-enter new password** fields and click **Set Password**.
3. In the logon screen, type the password of the nutanix user and press **Enter**.
      .. Note:: 
         Default user of the Move UI is **nutanix**.

Move Dashboard
^^^^^^^^^^^^^^

The dashboard includes the following options:

- *Environment*. Displays all the added environments. Environments can be VMware ESXi, Nutanix AOS, Microsoft Hyper-V and Amazon Web Services. Click + Add Environment to add locations to add locations for migrations between them.
   For more information, refer to Adding vCenter Server or Standalone ESXi Host Environment, Adding a Nutanix AOS Cluster Environment, Adding an AWS Environment, Adding Hyper-V Environment, and Adding an Azure Environment.

- *Create a Migration Plan*. Set up the migration plan for one or more VMs you want to migrate to the target environment. A migration plan includes scheduling options but does not start the cutover process.
   For more information, refer to Creating a Migration Plan or Creating a Migration Plan (ESXi to ESXi) or Creating a Migration Plan or Creating a Migration Plan or Creating a Migration Plan (AWS to ESXi) or Creating a Migration Plan (AHV to AWS) or Creating a Migration Plan (Azure to AHV) or Creating a Migration Plan (Azure to ESXi).

- *Manage an Environment or Migration Plan*. Manage the existing environment or migration plans on the Move dashboard. You can Refresh, Edit, or Remove an environment, and Start, Pause, Resume, Cancel, Edit, or Delete the migration plans.
   For more information, refer to Environments and Migration Plan Management.

- *View Metrics*. View the metrics of Move appliance health.
- *Upgrade Software*. Upgrade to a new version of Move to use the latest available features.
   For more information, refer to Move Upgrade Management.

- *Download Support Bundle*. Generate and download a support bundle that you can send to Nutanix Support for assistance.
   For more information, refer to Move Support Bundle Collection.

- *Experience Improvement*. Participate to improve Nutanix Customer Experience.
- *Realtime Logs*. Check the real time logs for all the Move components.
- *Events*. Displays the list of events happening in Move.
- *Help*. Opens the latest version of the Move documentation.
- *Rest API Docs*. Opens the latest version of the Move API documentation
- *About Move*. Check the latest version of the Move.
- *Log Out*. Sign out of Move VM.

.. thumbnail:: image/dashboard-42.png

