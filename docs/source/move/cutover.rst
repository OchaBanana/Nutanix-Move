.. _cutover:

Performing Migration Cutover
****************************

When the migration plan is started and the seeding process is complete, you can cut over the selected VMs to the Nutanix Cluster on AHV cluster. You can monitor the VM migration progress by clicking the **Status** link.

About this task
"""""""""""""""

After VMs status are **Ready to Cutover**.
To perform the migration cutover, do the following:

Procedure
"""""""""

| 1. In the Move UI, click the **Ready to Cutover** status to display the list of available VMs.
|
| 2. To perform a cutover, select the VMs or group of VMs.
|
| 3. Click **Cutover**.
|    The cutover process performs the following VM actions.

        - Shuts down the VM
        - Takes the final snapshots for the VM and copying the final changes to Nutanix Cluster on AWS and AHV
        - Adds a note in the VM in the vCenter.
        - Disconnects the source VM network interfaces
        - Creates a VM in the target Nutanix Cluster on AWS and AHV cluster
        - Attaches the replicated disks to the VM
        - Powers on or off the VM (depends on the initial power state)
        - Runs the scripts to set the static IP address
|
| The cutover process begins immediately and takes a few minutes. Once cutover is complete, the VM is ready for use in the new Nutanix Cluster on AHV cluster.
| 
| 4. Log on to the AHV cluster, see the migrated VMs.
|
| 5. to check migrated VMs helth, click **Launch console** at the migrated VMs.
|
| 6. **Done**.

.. hint:: 
    Please see `Nutanix Support Portal <https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Move-v4_5:top-onetb-migration-r.html>`_ for Large Data Migration estimate time.


Takeaways
---------



