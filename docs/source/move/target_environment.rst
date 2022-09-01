.. _target_environment:

Add Target Environment
**********************

About this task
"""""""""""""""

To add a Nutanix AOS cluster environment, do the following:

Procedure
"""""""""

| 1. Log on to the Move UI.
|
| 2. Click **+ Add Environment** under Environments.
     
     .. image:: image/add-aos-environment.png
                :width: 300
                :align: center

|   The Add Environment window appears.
| 
| 3. Select **Nutanix AOS** as the target environment type.
|
| 4. Complete the indicated fields and click **Add**.
|    a. **Environment Name**: AHV-Target Cluster
|    b. **Nutanix Environment**: *<Cluster IP>*.
|    c. **User Name**: admin.
|    d. **Password**: *<Cluster password>*.

    The AOS environment is added to the Move UI and can be viewed in the Environments list in the left pane of the Move dashboard.
