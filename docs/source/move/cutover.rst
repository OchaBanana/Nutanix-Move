.. _cutover:

Performing Migration cutover
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

.. hint:: Performance Matrix for Large Data Migration
    Total migration size	Number of VMs	Size for each vDisks	Number of vDisks	Source I/O	Data churn	Network bandwidth	Migration time taken	Platform
Data seeding	Cutover	
2 TB	1	2 TB	1	No	No	10 G	190 minutes	Less than 5 minutes	NX-3040-G4 (All Flash)
2 TB	1	512 GB	4	No	No	10 G	90 minutes	Less than 5 minutes	NX-3040-G4 (All Flash)
2 TB	1	256 GB	8	No	No	10 G	80 minutes	Less than 5 minutes	NX-3040-G4 (All Flash)
2 TB	20	100 GB	20	No	No	10 G	90 minutes	Less than 5 minutes	NX-3040-G4 (All Flash)
3.6 TB	1	Ranges from 1.5 TB to 2 GB	27	No	No	10 G	12 hours	5 minutes	NX-3060-G6
1 TB	1	1 TB	1	Yes	10 GB	1 G	418 minutes	28 minutes	NX-1065S
