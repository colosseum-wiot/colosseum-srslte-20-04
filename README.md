# colosseum-srslte-20-04
Colosseum srsLTE reporitory based on [srsLTE release_20_04](https://github.com/srsLTE/srsLTE). Timing advance estimation procedures and configuration files have been modified for srsLTE to work on Colosseum.

## Colosseum container
A container image with the code in this repository is provided to Colosseum users. The image, named `srslte-20-04`, is located in the Colosseum `common` images directory. The default image password is `ChangeMe`.

## How to use

### Automatic script
There is an automatic `colosseum_srslte.py` Python script in the `/root/radio_api` directory.
The script allows to run eNB, EPC and UE nodes, and to start a Colosseum RF scenario. Please note that eNB and UE nodes are supposed to run on different SRNs of Colosseum.

```
usage: colosseum_srslte.py [-h] [--enb] [--epc] [--ue]
                           [--rf-scenario RF_SCENARIO]

optional arguments:
  -h, --help                   show this help message and exit
  --enb                        run eNB node
  --epc                        run EPC node
  --ue                         run UE node
  --rf-scenario RF_SCENARIO    RF scenario to start
```

### Step-by-step instructions
#### Start Colosseum scenario
Select and start a Colosseum RF scanario, e.g., 1009.
On any of the SRNs of the experiment run:
`colosseumcli rf start 1009 -c`

The list of available scenarios can be consulted with:
`colosseumcli rf scenario list`

#### Start LTE nodes
srsLTE configuration files are stored in `radio_code/srslte_config`

##### Run EPC and eNB on SRN 1:
- Run srsEPC in a first terminal window:
  - `cd radio_code/srslte_config`
  - `srsepc epc.conf`
- Run srsENB in a second terminal window:
  - `cd radio_code/srslte_config`
  - `srsenb enb.conf`

##### Run UE on SRN 2:
- Run srsUE in a terminal window:
  - `cd radio_code/srslte_config`
  - `srsue ue.conf`
