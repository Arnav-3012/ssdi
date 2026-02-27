import streamlit as st
import numpy as np
from scipy.stats import t

def one_sample_t_test(data, pop_mean):
    data = np.array(data, dtype=float)
    n = len(data)
    df = n - 1
    
    x_bar = np.mean(data)
    sd = np.std(data, ddof=1)
    se = sd / np.sqrt(n)
    
    t_cal = (x_bar - pop_mean) / se
    p_val = 1 - t.cdf(t_cal, df)

    return t_cal, p_val



st.title("One Sample T-Test Calculator")

st.write("Enter sample data separated by commas")

data_input = st.text_input("Sample Data", "110, 112, 108, 115, 109")

pop_mean = st.number_input("Population Mean (μ₀)", value=108.0)

if st.button("Calculate"):
    try:
        data_list = [float(x.strip()) for x in data_input.split(",")]
        t_stat, p_value = one_sample_t_test(data_list, pop_mean)

        st.subheader("Results")
        st.write(f"T-statistic: {t_stat:.4f}")
        st.write(f"P-value: {p_value:.4f}")

        if p_value < 0.05:
            st.success("Reject the null hypothesis (significant result)")
        else:
            st.info("Fail to reject the null hypothesis")

    except:
        st.error("Invalid input. Please enter numbers separated by commas.")