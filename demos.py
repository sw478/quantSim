import numpy as np
import sys
from gate import Gate
from sim import Sim


def sim_demo():
    sim = Sim(3, "Demo")

    sim.add_gate(Gate.H(), [0])
    sim.add_gate(Gate.H(), [1])
    sim.add_gate(Gate.Toffoli(), [0, 1, 2])
    sim.add_gate(Gate.Swap(), [1, 2])
    sim.add_gate(Gate.H(), [2])

    sim.print_sim()
    sim.print_prob_dist()
    sim.print_statevector()


# Bell State Simulation
def sim_bell_state():
    sim = Sim(2, "Bell State")

    sim.add_gate(Gate.H(), [0])
    sim.add_gate(Gate.CX(), [0, 1])

    sim.print_sim()
    sim.print_prob_dist()
    sim.print_statevector()


def main():
    sim_bell_state()
    sim_demo()


if __name__ == "__main__":
    np.set_printoptions(threshold=sys.maxsize)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
    main()