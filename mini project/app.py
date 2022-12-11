import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

st.set_page_config(page_title=None, page_icon=None, layout="wide")

def load_data():
    placement= pd.read_csv('Placement_Data_Full_Class.csv')
    placement['salary'].fillna(value=0, inplace=True)
    placement.drop(['sl_no','ssc_b','hsc_b'], axis = 1,inplace=True) 
    return placement

st.title("Student Recruitment Analysis")
plt.style.use('seaborn-white')
placement_copy = None
with st.spinner("Data is Loading"):
    placement_copy = load_data()
if st.checkbox("View Dataset"):
    st.dataframe(placement_copy)
fig = plt.figure(figsize = (15, 10))
st.header("Placement Statistics for various level of education")
ax=plt.subplot(221)
plt.boxplot(placement_copy['ssc_p'])
ax.set_title('Secondary school percentage')
ax=plt.subplot(222)
plt.boxplot(placement_copy['hsc_p'])
ax.set_title('Higher Secondary school percentage')
ax=plt.subplot(223)
plt.boxplot(placement_copy['degree_p'])
ax.set_title('UG Degree percentage')
ax=plt.subplot(224)
plt.boxplot(placement_copy['etest_p'])
ax.set_title('Employability percentage')
st.pyplot(fig)

st.header("Data Filtering")
st.info("High School data after removing outliers")
Q1 = placement_copy['hsc_p'].quantile(0.25)
Q3 = placement_copy['hsc_p'].quantile(0.75)
IQR = Q3 - Q1    #IQR is interquartile range. 
filter = (placement_copy['hsc_p'] >= Q1 - 1.5 * IQR) & (placement_copy['hsc_p'] <= Q3 + 1.5 *IQR)
placement_filtered=placement_copy.loc[filter]
fig = plt.figure(figsize = (15, 5))
# plt.style.use('seaborn-white')
ax=plt.subplot(121)
plt.boxplot(placement_copy['hsc_p'])
ax.set_title('Before removing outliers(hsc_p)')
ax=plt.subplot(122)
plt.boxplot(placement_filtered['hsc_p'])
ax.set_title('After removing outliers(hsc_p)')
st.pyplot(fig)

st.header('Category wise analysis')
st.info("MBA degree student count graph")
plt.figure(figsize = (15, 7))
ax=sns.countplot(x="specialisation", data=placement_filtered, linewidth=5,edgecolor=sns.color_palette("magma", 3))
fig = plt.gcf()
ax.set_xticklabels(ax.get_xticklabels(),fontsize=12)
st.pyplot(fig)

st.info("Work experience data graph")
plt.figure(figsize = (15, 7))
ax=sns.countplot(x="workex", data=placement_filtered, linewidth=5,edgecolor=sns.color_palette("magma", 3))
fig = plt.gcf()
ax.set_xticklabels(ax.get_xticklabels(),fontsize=12)
st.pyplot(fig)

st.info("Degree graph")
plt.figure(figsize = (15, 7))
ax=sns.countplot(x="degree_t", data=placement_filtered, linewidth=5,edgecolor=sns.color_palette("magma", 3))
fig = plt.gcf()
ax.set_xticklabels(ax.get_xticklabels(),fontsize=12)
st.pyplot(fig)

st.info("Gender graph")
plt.figure(figsize = (15, 7))
ax=sns.countplot(x="gender", data=placement_filtered, linewidth=5,edgecolor=sns.color_palette("magma", 3))
fig = plt.gcf()
ax.set_xticklabels(ax.get_xticklabels(),fontsize=12)
st.pyplot(fig)

st.info("Highschool graph")
plt.figure(figsize = (15, 7))
ax=sns.countplot(x="hsc_s", data=placement_filtered, linewidth=5,edgecolor=sns.color_palette("magma", 3))
fig = plt.gcf()
ax.set_xticklabels(ax.get_xticklabels(),fontsize=12)
st.pyplot(fig)

st.info("Recruitment Status graph")
plt.figure(figsize = (15, 7))
ax=sns.countplot(x="status", data=placement_filtered, linewidth=5,edgecolor=sns.color_palette("magma", 3))
fig = plt.gcf()
ax.set_xticklabels(ax.get_xticklabels(),fontsize=12)
st.pyplot(fig)

st.header("Salary distribution graph")
sns.set(rc={'figure.figsize':(12,8)})
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

placement_placed = placement_filtered[placement_filtered.salary != 0]
sns.boxplot(placement_placed["salary"], ax=ax_box)
sns.distplot(placement_placed["salary"], ax=ax_hist)
# Remove x axis name for the boxplot
ax_box.set(xlabel='')
st.pyplot(f)


st.header("distributuin data of each data column")
plt.figure(figsize = (15, 7))
plt.style.use('seaborn-white')
plt.subplot(231)
sns.distplot(placement_filtered['ssc_p'])
fig = plt.gcf()
fig.set_size_inches(10,10)

plt.subplot(232)
sns.distplot(placement_filtered['hsc_p'])
fig = plt.gcf()
fig.set_size_inches(10,10)

plt.subplot(233)
sns.distplot(placement_filtered['degree_p'])
fig = plt.gcf()
fig.set_size_inches(10,10)

plt.subplot(234)
sns.distplot(placement_filtered['etest_p'])
fig = plt.gcf()
fig.set_size_inches(10,10)

plt.subplot(235)
sns.distplot(placement_filtered['mba_p'])
fig = plt.gcf()
fig.set_size_inches(10,10)

plt.subplot(236)
sns.distplot(placement_placed['salary'])
fig = plt.gcf()
fig.set_size_inches(10,10)

st.pyplot(fig)

st.header("What gets you Placements?")
st.info("Work Experience and Placement")
f,ax=plt.subplots(1,2,figsize=(18,8))
placement_filtered['workex'].value_counts().plot.pie(explode=[0,0],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Work experience')
sns.countplot(x = 'workex',hue = "status",data = placement_filtered)
ax[1].set_title('Influence of experience on placement')
st.pyplot(f)

st.info("Highschool Stream and Placement")
f,ax=plt.subplots(1,2,figsize=(18,8))
placement_filtered['hsc_s'].value_counts().plot.pie(explode=[0,0,0],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Highschool Stream')
sns.countplot(x = 'workex',hue = "status",data = placement_filtered)
ax[1].set_title('Influence of experience on placement')
st.pyplot(f)

st.info("Degree Stream and Placement")
f,ax=plt.subplots(1,2,figsize=(18,8))
placement_filtered['degree_t'].value_counts().plot.pie(autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Degree Stream')
sns.countplot(x = 'degree_t',hue = "status",data = placement_filtered)
ax[1].set_title('Influence of experience on placement')
st.pyplot(f)

st.info("MBA specialization and Placement")
f,ax=plt.subplots(figsize=(18,8))
sns.boxplot(y = "status",x = 'mba_p',data = placement_filtered, whis=np.inf,ax=ax)
sns.swarmplot(y = "status",x = 'mba_p',data = placement_filtered, size = 7,ax=ax,color = 'black')
sns.despine()
st.pyplot(f)


gapminder=px.data.gapminder()
fig = px.scatter(placement_filtered,x="mba_p",y="etest_p",color="status",facet_col="workex")
st.plotly_chart(fig, use_container_width=True)

fig = px.violin(placement_placed,y="salary",x="specialisation",color="gender",box=True,points="all")
st.plotly_chart(fig,use_container_width=True)


# run
# streamlit run app.py