streamlit run streamlit_app.py
import streamlit as st # type: ignore

def main():
    st.title("UK Domicile and Tax Residency Calculator")
    
    # Step 1: Were you born in the UK?
    born_in_uk = st.radio("Were you born in the UK?", ("Yes", "No"))

    if born_in_uk == "Yes":
        father_domiciled_uk = st.radio("Was your father domiciled in the UK at your birth?", ("Yes", "No"))
        
        if father_domiciled_uk == "Yes":
            st.success("Likely UK Domicile of Origin")
            return
        else:
            established_permanent_home_outside_uk = st.radio("Have you established a permanent home outside the UK?", ("Yes", "No"))
            
            if established_permanent_home_outside_uk == "Yes":
                st.success("Possible Domicile of Choice outside the UK")
            else:
                st.warning("Deemed UK Domicile (15 of last 20 years)")

    else:
        established_permanent_home_outside_uk = st.radio("Have you established a permanent home outside the UK?", ("Yes", "No"))

        if established_permanent_home_outside_uk == "Yes":
            st.success("Possible Domicile of Choice outside the UK")
        else:
            st.warning("Deemed UK Domicile (15 of last 20 years)")

    # Proceed to Statutory Residence Test
    st.subheader("Statutory Residence Test")
    
    spent_183_days = st.radio("Have you spent more than 183 days in the UK this tax year?", ("Yes", "No"))

    if spent_183_days == "Yes":
        st.error("UK Tax Resident")
        return
    else:
        permanent_home_uk = st.radio("Do you have a permanent home in the UK?", ("Yes", "No"))

        if permanent_home_uk == "Yes":
            close_family_ties = st.radio("Do you have close family ties in the UK?", ("Yes", "No"))
            
            if close_family_ties == "Yes":
                st.error("UK Tax Resident")
            else:
                st.success("Non-UK Tax Resident")
        else:
            st.success("Non-UK Tax Resident")

if __name__ == "__main__":
    main()