.. _move_deployment:

Move Deployment
***************

Nutanix recommends to deploy the Move VM on the AHV target through CLI or Prism Element UI.

    .. note::

        As a best practice, it is recommended to deploy Move on the target cluster (AHV or ESXi on AOS).


Deploying Move on AHV (Prism Element UI)
----------------------------------------

You can deploy the Move VM from the Prism Element UI. Deploying the Move VM creates, uploads, and starts the Move VM.


Before you begin
""""""""""""""""

To reduce the bandwidth, this lab downloaded the Move software package called **"move.qcow2"**.
For more information, refer to `Nutanix Support Portal <https://portal.nutanix.com/page/downloads?product=move>`_.


Procedure
"""""""""

| 1. Log on to the AHV cluster to deploy Move by using your Prism Element admin credentials.
|
| 2. Click the gear icon pull-down list of the main menu.
|
| 3. Click **Image Configuration**.
|     "move.qcow2" in Image Configuration window is displayed.
|
| 4. Go to **Home > VM**.
|
| 5. Click **+ Create VM**
|     The Create VM window appears.
|
| 6. Complete the indicated fields for creating a VM.
|     - **Name**: MoveVM-*<Your name>*.
|     - **Description** (optional): *leave blank*.
|     - **Timezone**: *leave default*.
|     - **Use this VM as an agent VM**: *leave uncheck*.
|     - **vCPU(s)**: *2*.
|     - **Number of Cores per vCPU**: *2*.
|     - **Memory**: *8*.
|     - **NIC**: *primary*
|
| 7. Remove the current CDROM disk by clicking the **X** next to the CDROM.
|
| 8. Click **+ Add New Disk** and select **Operation > Clone from Image Service**, and then in the **Image** drop-down, select **"move.qcow2"** image. Click **Add**.
|
| 9. Click the **Table** view and locate and select your **Move VM**, and then click **Power On**.
|
| 10. Wait for the VM to detect an IP address.
|     The new Move VM is powered ON.

.. tip::
    Now you can access to the Move user interface (UI) using the Move VM IP address or the FQDN.