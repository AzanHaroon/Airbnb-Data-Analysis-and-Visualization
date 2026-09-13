import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Airbnb Analytics Dashboard", page_icon="🏠", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("airbnb.csv")
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    df["rating_numeric"] = pd.to_numeric(df["rating"], errors="coerce")
    df["reviews_numeric"] = pd.to_numeric(df["reviews"], errors="coerce").fillna(0)
    for c in ["price","bathrooms","beds","guests","toiles","bedrooms","studios"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["country"] = df["country"].astype(str).str.strip()
    df["host_name"] = df["host_name"].fillna("Unknown")
    df["rating_status"] = np.where(df["rating_numeric"].isna(), "New", "Rated")
    return df

df = load_data()

st.title("Airbnb Data Analysis & Visualization")
st.caption("Interactive dashboard built from the supplied Airbnb listings dataset. Price is shown in dataset units because no currency column is provided.")

with st.sidebar:
    st.header("Filters")
    countries = sorted(df["country"].dropna().unique())
    selected = st.multiselect("Country", countries, default=[])
    guest_min, guest_max = int(df.guests.min()), int(df.guests.max())
    guests = st.slider("Guest capacity", guest_min, min(20, guest_max), (guest_min, min(6, guest_max)))
    price_cap = int(df.price.quantile(.99))
    price_range = st.slider("Price (dataset units)", int(df.price.min()), price_cap, (int(df.price.min()), price_cap))
    rating_filter = st.selectbox("Rating status", ["All", "Rated", "New"])

filtered = df.copy()
if selected:
    filtered = filtered[filtered.country.isin(selected)]
filtered = filtered[filtered.guests.between(*guests)]
filtered = filtered[filtered.price.between(*price_range)]
if rating_filter != "All":
    filtered = filtered[filtered.rating_status == rating_filter]

c1,c2,c3,c4 = st.columns(4)
c1.metric("Listings", f"{len(filtered):,}")
c2.metric("Median Price", f"{filtered.price.median():,.0f}" if len(filtered) else "—")
c3.metric("Avg Rating", f"{filtered.rating_numeric.mean():.2f}" if filtered.rating_numeric.notna().any() else "—")
c4.metric("Countries", f"{filtered.country.nunique():,}")

tab1, tab2, tab3 = st.tabs(["Overview", "Market Analysis", "Data Explorer"])

with tab1:
    left,right=st.columns(2)
    with left:
        st.subheader("Top Countries")
        cc=filtered.country.value_counts().head(10).sort_values()
        fig,ax=plt.subplots()
        cc.plot(kind="barh",ax=ax)
        ax.set_xlabel("Listings"); ax.set_ylabel("")
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
    with right:
        st.subheader("Price Distribution")
        p99=filtered.price.quantile(.99) if len(filtered) else 0
        vals=filtered.loc[filtered.price <= p99,"price"]
        fig,ax=plt.subplots()
        vals.plot(kind="hist",bins=35,ax=ax)
        ax.set_xlabel("Price (dataset units)")
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

with tab2:
    st.subheader("Median Price by Guest Capacity")
    cap=filtered.groupby("guests").price.median().loc[lambda s: s.index<=12]
    fig,ax=plt.subplots()
    cap.plot(kind="bar",ax=ax)
    ax.set_xlabel("Guests"); ax.set_ylabel("Median price")
    st.pyplot(fig, use_container_width=True); plt.close(fig)
    st.subheader("Country Summary")
    summary=(filtered.groupby("country")
             .agg(Listings=("id","count"), Median_Price=("price","median"),
                  Avg_Rating=("rating_numeric","mean"), Avg_Reviews=("reviews_numeric","mean"))
             .sort_values("Listings",ascending=False).head(20))
    st.dataframe(summary.round(2), use_container_width=True)

with tab3:
    st.subheader("Filtered Listings")
    cols=["id","name","host_name","address","country","price","rating","reviews","guests","beds","bedrooms","bathrooms"]
    st.dataframe(filtered[cols].head(1000), use_container_width=True)
    st.download_button("Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"), "airbnb_filtered.csv", "text/csv")

st.divider()
st.markdown("**Project note:** This dashboard is an analytical visualization of the supplied dataset, not a live Airbnb service.")
