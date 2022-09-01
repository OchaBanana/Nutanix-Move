.. _test_mp:

Test VMs Migration Plan
***********************

You can test the VMs on the target environment prior to the final cutover. During the final cutover, the source VMs are powered off which disrupts the underlying data replication. You can test multiple VMs with this feature without disrupting the source VMs. After the test, you can continue with the final cutover in your production environment.

About this task
"""""""""""""""

to test the VMs that migrated to Target cluster can run and operated normally before final cutover, do the following:


Procedure
"""""""""

| 1. Make sure all VMs migration status changes to **Ready to Cutover**, the following actions are enabled:
|    

    - **Test Actions**: Click to continue with testing the VMs on the target environment.
    - **Cutover** : Click to continue with normal migration process in the production environment.


| 2. Select **Create Test VM** from the **Test Actions** drop-down. The source VMs remain powered on and a test VM is created in the target environment.
This process takes some time.

     .. image:: image/test-actions.png
                :width: 500
                :align: center

| 3. Click **Continue** on the dialog box.

     .. image:: image/test-vm-confirm.png
                :width: 300
                :align: center

| 4. Click **View Test VM** option created under the Migration Status tab under **Ready to Cutover**.

     .. image:: image/test-actions-view.png
                :width: 300
                :align: center

| The following options are enabled after you click **Test Actions**:
|
    - **Recreate Test VM**: Click to recreate a test VM.
    - **Remove Test VM**: Click to remove the deployed test VMs from the target and changes the VM status back to Ready to Cutover.

| 5. Click **View Test VM**.
|    A new window for the target network opens up.
|
| 6. Enter the credentials of the source VM to log on.
|
| 7. Look for the test VM and perform test operations.
|

    .. note::
            Test VMs are suffixed with -MoveTest in the target network.


| 8. Once you test the VMs in the target environment, come back to the Move Dashboard and click **Remove Test VM** to clean up the target environment.
