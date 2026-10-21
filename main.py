
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks = np.array([
    [80, 75, 90],
    [70, 85, 80],
    [90, 95, 85],
    [60, 70, 75]
])
print("Student averages:", marks.mean(axis=1))
print("Shape:", marks.shape)
print("Subject averages:", marks.mean(axis=0))
print("Grace marks:\n", marks + 5)
print("Weighted scores:", np.dot(marks, [0.3, 0.3, 0.4]))
df = pd.read_csv("employees.csv")
print(df.info())
print(df.describe())
print(df.loc[0])
print(df.iloc[0:2])
print(df[df["department"] == "IT"])
df = df.drop_duplicates()
df["salary"] = df["salary"].fillna(df["salary"].median())
df["salary"] = df["salary"].astype(int)
summary = df.groupby("department").agg(
    Headcount=("employee_id", "count"),
    Average_Salary=("salary", "mean"),
    Maximum_Salary=("salary", "max")
)
print("\nHeadcount:", end=" ")
for dept in ["Sales", "HR", "IT", "Finance"]:
    print(f"{dept} {summary.loc[dept, 'Headcount']}", end=" | ")
print()
departments = pd.read_csv("departments.csv")
inner = pd.merge(df, departments, on="department", how="inner")
left = pd.merge(df, departments, on="department", how="left")
outer = pd.merge(df, departments, on="department", how="outer")
print("\nOuter join:")
print(outer[["name", "department", "head", "budget"]].to_string(index=False))
no_employees = departments[
    ~departments["department"].isin(df["department"])
]
print("Department with no employees:", no_employees["department"].iloc[0])
summary["Average_Salary"].plot(kind="bar", title="Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.legend(["Average Salary"])
plt.tight_layout()
plt.savefig("bar.png")
plt.close()
plt.hist(df["salary"], label="Salary")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Employees")
plt.legend()
plt.savefig("histogram.png")
plt.close()
plt.scatter(df["age"], df["salary"], label="Employees")
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.savefig("scatter.png")
plt.close()
plt.plot(df["employee_id"], df["salary"], marker="o", label="Salary")
plt.title("Salary by Employee ID")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.savefig("line.png")
plt.close()


