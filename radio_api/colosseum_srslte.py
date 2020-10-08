import argparse
import os
import subprocess


# compose tmux command to run for specified node_type
def tmux_command(node_type: str, t_session: str) -> str:

    config_dir = '/root/radio_code/srslte_config/'

    config_file = node_type + '.conf'
    cmd = 'cd ' + config_dir + ' && srs' + node_type + ' ' +\
        config_dir + config_file

    return 'tmux send -t ' + t_session + ' "' + cmd + '" ENTER'


# start specified node_type
def start_node(node_type: str, t_session:str, t_split: bool) -> bool:

    tmux_split_window = 'tmux split-window -h -t ' + t_session + '.right'

    # split tmux_session
    if t_split:
        subprocess.run(tmux_split_window, shell=True)

    subprocess.run(tmux_command(node_type, t_session), shell=True)
    print('Started ' + node_type + ' application')

    return True


if __name__ == '__main__':

    tmux_split = False
    tmux_session = 'colosseum-srslte'

    parser = argparse.ArgumentParser()
    parser.add_argument('--enb', help='run eNB node', action='store_true')
    parser.add_argument('--epc', help='run EPC node', action='store_true')
    parser.add_argument('--ue', help='run UE node', action='store_true')
    parser.add_argument('--rf-scenario', type=int, help='RF scenario to start')
    args = parser.parse_args()

    if not (args.enb or args.epc or args.ue):
        print("Please specify node(s) to start")
        exit(1)
    elif args.enb and args.ue:
        print('Base station and user applications should be instantiated on different SRNs')
        exit(1)

    # start RF scenario
    if args.rf_scenario:
        print('Starting RF scenario ' + str(args.rf_scenario))
        os.system('colosseumcli rf start ' + str(args.rf_scenario) + ' -c')
        # subprocess.Popen([scenario_cmd], stdout=subprocess.PIPE, shell=True)
    else:
        print('WARNING: RF scenario not specified')

    # kill existing tmux session, if any
    os.system('tmux kill-session -t ' + tmux_session)

    # start new tmux session
    tmux_create_session = 'tmux new-session -d -s ' + tmux_session
    subprocess.run(tmux_create_session, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if args.epc:
        # start epc
        tmux_split = start_node('epc', tmux_session, tmux_split)

    if args.enb:
        # start enb
        tmux_split = start_node('enb', tmux_session, tmux_split)
    elif args.ue:
        # start ue
        tmux_split = start_node('ue', tmux_session, tmux_split)
