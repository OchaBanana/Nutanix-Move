.. _create__mp:

Creating a Migration Plan
*************************

You can create a migration plan to seed the data, cutover, and monitor the VMs. You can create the migration plan in Move UI without initiating the cutover process.

About this task
"""""""""""""""

To create a migration plan, do the following:

Procedure
"""""""""

| 1. Log on to the Move VM.
|
| 2. On the Move dashboard, click **Create a Migration Plan**.
|    The Enter Migration Plan Name window appears.
|
| 3. Enter the new migration plan name, and then click **OK**.
|    The New Migration Plan window appears.
|
| 4. Complete the following fields, and then click **Next**.
|    a. **Select a Source**: ESXi-Source Cluster
|    b. **Select a Target**: AHV-Target Cluster
|    C. **Target Containers**: *<Your name>*-ctn
|
| 5. In the Select VMs screen, select '*<Your name>*-win-vm' and '*<Your name>*-linux-vm' from the list. To add all the VMs, click **+Add All**, and then click **Next**.
|    You can filter the VMs by name in the Filter bar. You can also sort the VM types by selecting the appropriate column.
 
        .. note::
            You cannot add more than 50 VMs in a single migration plan.

|    The selected VMs are displayed in the sidebar.
|
| 6. In the Network Configuration screen, select the 'primary' network. Then, click **Next**.
|
| 7. In the VM Preparation screen, select '**Autometic**' modes.
 
        .. note::
            | **Automatic**. Move automatically runs scripts on the source VMs to prepare them for migration.
            | **Manual**. Move displays the VM preparation scripts for Windows and Linux VMs.
            | These scripts prepare the source VMs by performing the following.
            - Installs NTNX VirtIO driver
            - Runs the IP address retention script
            - Runs Set SAN policy script
            - Runs uninstall VMware tools script

        .. note::
            Uninstalling VMware tools from the migrated VMs is on a best-effort basis.

|
| 8. Provide the credentials of the source VMs under Windows VMs or Linux VMs, depending on the type of the source VM. Then, click **Next**.
|
| 9. To save the migration plan, click **Save**.
 
        .. note::
            | **Back**: To edit the information, click this option.
            | **Save**: To save the migration plan, click this option.
            |            For more information about how to start the migration later, and check the migrated VM status and details, refer to Environments and Migration Plan Management.
            | **Save and Start**: Click this option to save the migration plan and begin the migration immediately.

|    The seeding process for migration begins. You can monitor this information by selecting **Status** for the migration plan.
