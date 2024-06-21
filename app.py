import streamlit as st

# Title and description
st.title('Simple Calculator')
st.write('Enter two numbers and select an operation.')

# User input for two numbers
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

# Operation selection
operation = st.selectbox(
    'Select the operation:',
    ('Addition', 'Subtraction', 'Multiplication', 'Division')
)

# Perform selected operation
if operation == 'Addition':
    result = num1 + num2
    st.write(f'The result of {num1} + {num2} = {result}')
elif operation == 'Subtraction':
    result = num1 - num2
    st.write(f'The result of {num1} - {num2} = {result}')
elif operation == 'Multiplication':
    result = num1 * num2
    st.write(f'The result of {num1} * {num2} = {result}')
elif operation == 'Division':
    if num2 == 0:
        st.error('Division by zero is not allowed')
    else:
        result = num1 / num2
        st.write(f'The result of {num1} / {num2} = {result}')
