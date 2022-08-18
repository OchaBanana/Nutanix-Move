.. _source_environment:

Add Source Environment
**********************

Before you begin
""""""""""""""""

You must consider the supported guest operating systems, requirements, recommendations, unsupported features, and limitations provided in this section before starting the migration process.
For more information please see `Nutanix Support Portal <https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Move-v4_5:top-migration-considerations-c.html>`_.

About this task
"""""""""""""""

To add a vCenter Server or standalone ESXi host environment, do the following:

Procedure
"""""""""

| 1. Log on to the Move UI.
|
| 2. Click **+ Add Environment** under Environments.
|   The Add Source Environment window appears.


        .. thumbnail:: image/add-esxi-environment.png
                :width: 300
                :align: center
                
| 3. Select **VMware ESXi** as the environment type.
|
| 4. Complete the indicated fields and click **Add**.
|    a. **Environment Name**: ESXi-Source Cluster.
|    b. **vCenter Server or standalone ESX host**: Enter *<vCenter IP>*
|    c. **User Name**: Enter the *<vCenter username>*.
|    d. **Password**: Enter the *<vCenter password>*.
| 
| The VMware ESXi environment is added to the Move UI and can be viewed in the Environments list in the left pane of the Move dashboard.