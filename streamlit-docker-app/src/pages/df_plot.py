import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def f1(x, omiga):
    return x + omiga * ((18 - 7 * x) / np.sin(x) - x)  # 迭代格式1


def f(x):
    return x * np.sin(x) + 7 * x - 18  # 超越方程


@st.cache
def sol_trans_eqa(eps, x0):
    """
    solve transcendental equation
    eps: precision
    x0： Initial point
    """
    flag = True
    sol1 = []
    k = 0  # 迭代次数
    while abs(f(x0)) > eps:
        x0 = f1(x0, 0.1)
        k = k + 1
        sol1.append(f(x0))
        if k > 10000:
            flag = False
            break
    return flag, k, x0, sol1


def app():
    st.markdown("## 松弛迭代法求超越方程零根")
    st.latex("x * sin(x) + 7 x - 18")
    eps = st.number_input("精度", value=0.0000001)
    x0 = st.number_input("初始点", value=4)

    flag, k, x0, sol1 = sol_trans_eqa(eps, x0)
    if flag:
        # mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
        mpl.rcParams["axes.unicode_minus"] = False
        fig = plt.figure(figsize=(16, 8))
        plt.plot(sol1, lw=2, color="b", marker="o", label="format1")  # 绘制迭代格式1函数曲线
        plt.xlim(0, 30)
        plt.legend()
        plt.title("Process of Convergence")
        st.write("x0 is", x0, "迭代次数: ", k)
        st.pyplot(fig)
    else:
        st.write("此迭代格式发散")
