"""
Dashboard_forex is licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Copyright (c) 2023 TF-2022. All rights reserved.
"""

import streamlit as st
st.set_page_config(page_title= "Home",
                   page_icon= "🏡")
st.title("Dashboard Forex")
st.warning("Page en construction")

def main_home() :
    from app.home.theme import Theme_fond
    Theme_fond()

if __name__ == '__main__':
    main_home()
