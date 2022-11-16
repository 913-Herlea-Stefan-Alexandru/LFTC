from domain.Fa import Fa


def print_menu():
    print("1. See states")
    print("2. See alphabet")
    print("3. See start state")
    print("4. See end states")
    print("5. See transitions")
    print("6. Verify sequence")
    print("0. exit")


if __name__ == "__main__":
    fa = Fa("fa.in")
    is_running = True

    while is_running:
        print_menu()
        cmd = input(">> ")

        try:
            cmd = int(cmd)
        except Exception:
            print("\nInvalid command\n")
            continue

        if cmd == 1:
            print(fa.get_states())
        elif cmd == 2:
            print(fa.get_alphabet())
        elif cmd == 3:
            print(fa.get_start())
        elif cmd == 4:
            print(fa.get_end())
        elif cmd == 5:
            transitions = fa.get_transitions()
            for transition in transitions:
                print(str(transition) + ": " + str(transitions[transition]))
        elif cmd == 6:
            sequence = input("Enter sequence: ")
            print("Sequence is valid for FA" if fa.verify_sequence(sequence) else "Sequence is invalid for FA")
        elif cmd == 0:
            is_running = False
        else:
            print("\nInvalid command\n")
