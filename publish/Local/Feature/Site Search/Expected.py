import constants
WRAPPER_HIDDEN_FIELD_SELECTOR_VALUE_MAP = {
    "pageSize": "3",
    "readMoreText": "Read More",
    "downloadText": "Download",
    "showMoreResultsText": "Show More",
    "showingText": "Showing",
    "ofText": "Of",
    "noMoreResult": "No more result to load",
    "itemsText": "Results",
    "selectedFilterResultText": "Applied Items",
    "noResultText" : "No Search Result Found",
    "clearAllLabel": "Clear",
    "applyFilterLabel": "Applied all filters",
    "closeBtnLabel": "Close",
    "hideSortByDate": "false"
}
UI_CONFIGURATIONS_SELECTORS_TEXT = {
    "div.onsitesearch__searchbox h2": "Automation | Search Title",
    "li#AllSectionsTab a": "All Sections \n(4380)",
    "li#ProductsTab a": "Products \n(465)",
}

UI_CONFIGURATIONS_SELECTORS_ATTRIBUTE = {
    "li#AllSectionsTab": {
        "data-value": "All Sections",
    },
    "li#AllSectionsTab a": {
        "data-type": "ALL",
        "data-facets": "hbkworld:industry,hbkworld:application,hbkworld:services,hbkworld:content-type,hbkworld:training,hbkworld:language,hbkworld:product,hbkworld:search-v3",
        
    },
    "li#ProductsTab": {
        "data-value": "Products",
    },
    "li#ProductsTab a": {
        "data-type": "product-page,productoverview-page,productlisting-page,productoption-page",
        "data-facets": "hbkworld:product,hbkworld:application,hbkworld:industry",
        
    },
    "input#filterSearchPlaceholder":{
        "name": "filterSearchPlaceholder",
        "value": "Search Here"
    },
    "input#searchBox":{
        "name": "searchBox",
        "value": "true"
    },
}


UI_CONFIGURATIONS_SELECTORS_PLACEHOLDER = {
    "input.onsitesearch__searchboxbar__input": "Enter your search",
}

BASIC_HIT_ITEMS = {
    0:{
        "div.teaser-item__info p": "content",
        "div.teaser-item__info h2": "List - Text Only",
        "div.teaser-item__info p.teaser-item__info-details": "Plastics solutions expert, Novares boosts its capabilities with a new test centre and vibration shaker system for assessing vehicle parts",
    },
    1:{
        "div.teaser-item__info p": "content",
        "div.teaser-item__info h2": "Teaser Spacing",
        "div.teaser-item__info p.teaser-item__info-details": "Lorem Ipsum",
    },
    2:{
        "div.teaser-item__info p": "content",
        "div.teaser-item__info h2": "Top Bottom Spacing",
        "div.teaser-item__info p.teaser-item__info-details": "Lorem Ipsum",
    },
}

PRODUCT_TAB_HIT_ITEMS = {
    0:{
        "div.teaser-item__info p": "product",
        "div.teaser-item__info h2": "Product Performance",
        "div.teaser-item__info p.teaser-item__info-details": "Highlights box WEB(Custom trigger with custom cookie 1h).",
    },
    1:{
        "div.teaser-item__info p": "product",
        "div.teaser-item__info h2": "Fatigue Life Prediction and Test-CAE Correlation",
        "div.teaser-item__info p.teaser-item__info-details": "Explore key features of nCode",
    },
    2:{
        "div.teaser-item__info p": "product",
        "div.teaser-item__info h2": "ReliaSoft (Reliability Analysis and Management)",
        "div.teaser-item__info p.teaser-item__info-details": "Ready to take your reliability program furthe",
    },
}

HIT_ALPHABETICAL_SORT ={
    0:{
        "div.teaser-item__info p": "content",
        "div.teaser-item__info h2": "構造力学入門"
    },
    1:{
        "div.teaser-item__info p": "resource",
        "div.teaser-item__info h2": " Modal analysis and PULSE Reflex (Case Study, The University of Windsor)"
    },
    2:{
        "div.teaser-item__info p": "news",
        "div.teaser-item__info h2": "10 Tips to Make Your Strain Gauge Installations Go Quickly"
    },
}

HIT_DATE_SORT ={
    0:{
        "div.teaser-item__info p": "home",
        "div.teaser-item__info h2": "Home FEB01"
    },
    1:{
        "div.teaser-item__info p": "seminar",
        "div.teaser-item__info h2": "Seminar JAN05"
    },
    2:{
        "div.teaser-item__info p": "product listing",
        "div.teaser-item__info h2": "Tripods"
    },
}

SEARCH_AND_FILTER = {
    0:{
        "search_keyword": "HBK",
        "search_result": {
            0:{
                "div.teaser-item__info p": "content",
                "div.teaser-item__info h2": "List - Text Only"
            },
            1:{
                "div.teaser-item__info p": "content",
                "div.teaser-item__info h2": "List"
            },
            2:{
                "div.teaser-item__info p": "content",
                "div.teaser-item__info h2": "List"
            },
        }
    },
    1:{
        "search_keyword": "Brain Station 23",
        "search_result": {
            0:{
                "div.teaser-item__info p": "content",
                "div.teaser-item__info h2": "List - Text Only"
            },
            1:{
                "div.teaser-item__info p": "content",
                "div.teaser-item__info h2": "2020 HBK Technology Days"
            },
            2:{
                "div.teaser-item__info p": "article",
                "div.teaser-item__info h2": "Force Glossary"
            },
        },
        "search-facet" : 6
    },
    2:{
        "search_keyword": "Uganda",
    },
}

FACET_SEARCH_CONFIG ={
    "search-facet" : {
        "count": 6,
        0:{
            "data-name": "industry",
            "option_count": 8,
            "search_key_0": 'a',
            "search_key_0_count": 8,
            "search_key_1": 'u',
            "search_key_1_count": 3,
            "search_key_2": 'to',
            "search_key_2_count": 2,
            "select_item": [0,3],
            "refinement_items_select_0":[
                {
                    "index": '2',
                    "label": "Industry : Aerospace"
                }
            ],
            "refinement_items_select_1":[
                {
                    "index": '2',
                    "label": "Industry : Aerospace"
                },
                {
                    "index": '3',
                    "label": "Industry : Automotive"
                }
            ],
            "select_item_results_0": {
                0:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "2021 HBK Technology Days"
                },
                1:{
                    "div.teaser-item__info p": "overview",
                    "div.teaser-item__info h2": "Events"
                },
                2:{
                    "div.teaser-item__info p": "home",
                    "div.teaser-item__info h2": "Homepage - The product physics experts"
                },
            },
            "select_item_results_1": {
                0:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "2020 HBK Technology Days"
                },
                1:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "2021 HBK Technology Days"
                },
                2:{
                    "div.teaser-item__info p": "overview",
                    "div.teaser-item__info h2": "Events"
                },
            }
        },
        1:{
            "data-name": "application",
            "option_count": 13,
            "search_key_0": 'st',
            "search_key_0_count": 8,
            "search_key_1": 'ru',
            "search_key_1_count": 3,
            "search_key_2": 'to',
            "search_key_2_count": 2,
            "select_item": [0,2],
            "refinement_items_select_0":[
                {
                    "index": '2',
                    "label": "Application : Acoustics"
                }
            ],
            "refinement_items_select_1":[
                {
                    "index": '2',
                    "label": "Application : Acoustics"
                },
                {
                    "index": '3',
                    "label": "Application : Durability and Fatigue"
                }
            ],
            "select_item_results_0": {
                0:{
                    "div.teaser-item__info p": "overview",
                    "div.teaser-item__info h2": "Test page for sort by date"
                },
                1:{
                    "div.teaser-item__info p": "overview",
                    "div.teaser-item__info h2": "New copy Test page for sort by date"
                },
                2:{
                    "div.teaser-item__info p": "product listing", 
                    "div.teaser-item__info h2": "Random-On-Random"
                },
            },
            "select_item_results_1": {
                0:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "Lightweight Structural Integrity Testing"
                },
                1:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "Material Properties Testing"
                },
                2:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "QuantumX Integration in ZwickRoell Testing Machine"
                },
            }
        },
        2:{
            "data-name": "services",
            "option_count": 21,
            "search_key_0": 'en',
            "search_key_0_count": 8,
            "search_key_1": 'g',
            "search_key_1_count": 3,
            "search_key_2": 'to',
            "search_key_2_count": 2,
            "select_item": [2,6],
            "refinement_items_select_0":[
                {
                    "index": '2',
                    "label": "Services : Engineering Services"
                }
            ],
            "refinement_items_select_1":[
                {
                    "index": '2',
                    "label": "Services : Engineering Services"
                },
                {
                    "index": '3',
                    "label": "Services : Maintenance"
                }
            ],
            "select_item_results_0": {
                0:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "Residual Stresses | Residual Stress Measurement"
                },
                1:{
                    "div.teaser-item__info p": "article",
                    "div.teaser-item__info h2": "Product Sync - New Test"
                },
                2:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "HBK World Sprint 28"
                },
            },
            "select_item_results_1": {
                0:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "HBK Monitoring Solutions Overview"
                },
                1:{
                    "div.teaser-item__info p": "content",
                    "div.teaser-item__info h2": "Residual Stresses | Residual Stress Measurement"
                },
                2:{
                    "div.teaser-item__info p": "article",
                    "div.teaser-item__info h2": "Product Sync - New Test"
                },
            }
        }    
    }
}