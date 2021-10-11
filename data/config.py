""" COLUMNS DESCRIPTION """
macrodata2_colnames = ['tarix', 'year', 'months', 'ym', 'gdp', 'gdp_def', 'ngdp', 'rgdp', 'rngdp', 'cap_invest', 'nominc',
            'nomsal',
            'budrev', 'budrev/gdp', 'budexp', 'budexp/gdp', 'buddef', 'buddef/gdp', 'neer', 'nneer', 'reer', 'nreer',
            'cr_port', 'vkk', 'vkk_rate', 'cpi_change', 'cpi_chg_+1', 'cpi_cumul', 'usdazn', 'brend_oil_price']
macrodata2_coldesc = ['Date of the data (end of month)', 'Year', 'Month', 'Year and month values combines as string',
           'Gross Domestic Product', 'GDP default', 'Non-oil sector GDP', 'Real GDP', 'Real non-oil sector GDP',
           'Capital investments', 'Nominal income', 'Nominal salary', 'Budget revenues', 'Budget revenues GDP',
           'Budget expenditures', 'Budget expenditures', 'Budget expenditures GDP', 'Budget deficit',
           'Budget deficit GDP', 'Nominal effective exchange rate', 'Non-oil sector nominal effective exchange rate',
           'Real effective exchange rate', 'Non-oil sector real effective exchange rate',
           'Total loan portfolio of the banks', 'Total 30+ day overdue loan portfolio of the banks', 'vkk/cr_port',
           'Consumer price index change', 'Consumer price index change+1', 'CPI (not inflation)',
           'USDAZN exchange rate', 'Price of brand oil']

data_to_cols = {
    'm_macro': dict(zip(macrodata2_colnames, macrodata2_coldesc))
    # 'data_m_macro':
}
