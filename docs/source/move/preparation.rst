.. _preparation:

Preparation
***********

Before you start Depolying Move VM, you need to prepare source VMs and Storage Container to use in this Lab.

Create Windows VM
"""""""""""""""""

| 1. Log on to ESXi Cluster Prism Eliment.
|
| 2. Go to **Home > VM**.
|
| 3. Click at "Windows2016" VM, then click **Clone** under VM Table.
|    The Create VM window appears.
|
| 4. Complete the indicated fields for creating a VM.

     - **Number of Clones**: *1*.
     - **Name**: *<Your name>*-win-vm.

     - **vCPU(s)**: *1*.
     - **Number of Cores per vCPU**: *1*.
     - **Memory**: *4*.

     .. thumbnail:: image/clone-win-vm.png

|
| 5. Click **Save**.
|
| 6. Locate and select your **Wundows VM**, and then click **Power On**.


Create Linux VM
"""""""""""""""""


| 1. At **VM** Teble view click at "CentOS" VM, then click **Clone** under VM Table.
|    The Create VM window appears.
|
| 2. Complete the indicated fields for creating a VM.

     - **Number of Clones**: *1*.
     - **Name**: *<Your name>*-linux-vm.

     - **vCPU(s)**: *1*.
     - **Number of Cores per vCPU**: *2*.
     - **Memory**: *6*.

|
| 3. Click **Save**.
|
| 4. Locate and select your **Linux VM**, and then click **Power On**.


Create Target Container
"""""""""""""""""""""""

| 1. Log on to AHV Cluster.
|
| 2. Go to **Home > Storage**.

        .. thumbnail:: image/storage-menu.png

|
| 3. Click **+ Storage Container**
|     The Create Storage Container window appears.
|
| 4. Complete the indicated fields for creating a Storage Container.

     - **Name**: *<Your name>*-ctn.

     .. thumbnail:: image/create-ctn.png

|
| 5. Click **Save**.
|
| 9. Click the **Table** view and locate your **Storage Container**.
