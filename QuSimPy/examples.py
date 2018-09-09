from QuSimPy.QuSim import QuantumRegister

#############################################
#                 Introduction              #
#############################################
# Here Will Be A Few Example of Different   #
# Quantum States / Algorithms, So You Can   #
# Get A Feel For How The Module Works, and  #
# Some Algorithmic Ideas                    #
#############################################

#############################################
#            Quantum Mesurment              #
#############################################
# This experement will prepare 2 states, of a
# Single qubit, and of 5 qubits, and will just
# Measure them

OneQubit = QuantumRegister(1)  # New Quantum Register of 1 Qubit
print('One Qubit: ' + OneQubit.measure())  # Should Print 'One Qubit: 0'

FiveQubits = QuantumRegister(5)  # New Quantum Register of 5 Qubits
# Should Print 'Five Qubits: 00000'
print('Five Qubits: ' + FiveQubits.measure())

#############################################
#            Correct Notation               #
#############################################
# This Experement is the same as the last, but just puts the
# Correct Notation When Printed. (Its called Dirac or Bra-Ket Notation)

print('One Qubit (Correct Notation): |' + OneQubit.measure() + '>')
print('Five Qubits (Correct Notation): |' + FiveQubits.measure() + '>')

#############################################
#          Simple Quantum Experement        #
#############################################
# This experement will just apply a pauli-X / NOT Gate
# to a single qubit, and then measure!
# New Single Qubit Quantum Register, if mesured now it would result in 0
NOT = QuantumRegister(1)
NOT.applyGate('X', 1)  # Apply Pauli-X Gate

# Now we have a finished State, we can measure and print it to the console
print('NOT Gate: |' + NOT.measure() + '>')

#############################################
#                 Swap 2 Qubits             #
#############################################
# Here, We Will Apply a Pauli-X Gate / NOT Gate
# To the first qubit, and then after the algorithm,
# it will be swapped to the second qubit.

Swap = QuantumRegister(2)  # New Quantum Register of 2 qubits
Swap.applyGate('X', 1)  # Apply The NOT Gate. If Measured Now, it should be 10

# Start the swap algorithm
Swap.applyGate('CNOT', 1, 2)
Swap.applyGate('H', 1)
Swap.applyGate('H', 2)
Swap.applyGate('CNOT', 1, 2)
Swap.applyGate('H', 1)
Swap.applyGate('H', 2)
Swap.applyGate('CNOT', 1, 2)
# End the swap algorithm

print('SWAP: |' + Swap.measure() + '>')  # Measure the State, Should be 01

#############################################
#               Fair Coin Flip              #
#############################################
# Shown in this 'Experement', is a so called 'Fair Coin Flip',
# Where a state will be prepared, that has an equal chance of
# Flipping to Each Possible State. to do this, the Hadamard
# Gate will be used.

# New Quantum Register of 1 Qubit (As a coin has only 2 states)
FairCoinFlip = QuantumRegister(1)
# If measured at this point, it should be |0>

# Apply the hadamard gate, now theres an even chance of measuring 0 or 1
FairCoinFlip.applyGate('H', 1)

# Now, the state will be measured, flipping the state to
# either 0 or 1. If its 0, we will say "Heads", or if its
# 1, we will say "Tails"
FairCoinFlipAnswer = FairCoinFlip.measure()  # Now its flipped, so we can test
if FairCoinFlipAnswer == '0':
    print('FairCoinFlip: Heads')
elif FairCoinFlipAnswer == '1':
    print('FairCoinFlip: Tails')

#############################################
#             CNOT Gate                     #
#############################################
# In this experement, 4 states will be prepared, {00, 01, 10, 11}
# And then the same CNOT Gate will be run on them,
# To Show The Effects of the CNOT. The Target Qubit will be 2, and the control 1

# New Quantum Register of 2 Qubits, done 4 times.
# If any are measured at this time, the result will be 00
ZeroZero = QuantumRegister(2)
ZeroOne = QuantumRegister(2)
OneZero = QuantumRegister(2)
OneOne = QuantumRegister(2)

# Now prepare Each Into The State Based On Their Name
# ZeroZero Will be left, as thats the first state anyway
ZeroOne.applyGate('X', 2)
OneZero.applyGate('X', 1)
OneOne.applyGate('X', 1)
OneOne.applyGate('X', 2)

# Now, a CNOT Will Be Applied To Each.
ZeroZero.applyGate('CNOT', 1, 2)
ZeroOne.applyGate('CNOT', 1, 2)
OneZero.applyGate('CNOT', 1, 2)
OneOne.applyGate('CNOT', 1, 2)

# Print the results.
print('CNOT on 00: |' + ZeroZero.measure() + '>')
print('CNOT on 01: |' + ZeroOne.measure() + '>')
print('CNOT on 10: |' + OneZero.measure() + '>')
print('CNOT on 11: |' + OneOne.measure() + '>')


#############################################
#             Random Big Circut             #
#############################################
# This is just a big circut... No real point to it

Random = QuantumRegister(5)
Random.applyGate('H', 1)
Random.applyGate('Z', 2)
Random.applyGate('S', 3)
Random.applyGate('Z', 4)
Random.applyGate('SDagger', 5)
Random.applyGate('CNOT', 1, 2)
Random.applyGate('Y', 3)
Random.applyGate('S', 4)
Random.applyGate('Id', 5)
Random.applyGate('SDagger', 1)
Random.applyGate('X', 3)
Random.applyGate('H', 5)
Random.applyGate('S', 2)
Random.applyGate('CNOT', 5, 4)
Random.applyGate('Id', 1)
Random.applyGate('S', 2)
Random.applyGate('CNOT', 4, 3)
Random.applyGate('SDagger', 5)
Random.applyGate('T', 2)
Random.applyGate('T', 3)
Random.applyGate('TDagger', 2)

print('Big Circut: |' + Random.measure() + '>')
