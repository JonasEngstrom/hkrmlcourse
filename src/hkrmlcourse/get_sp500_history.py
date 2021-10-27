# get_sp500_history.py

import yfinance
import pandas

# The following string contains the tickers of the companies in the S&P 500
# according to https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
# which was retrieved at 2021-10-27 21.40 CEST, sorted alphabetically.
sp500_tickers = ("A AAL AAP AAPL ABBV ABC ABMD ABT ACN ADBE ADI ADM ADP ADSK "
                 "AEE AEP AES AFL AIG AIZ AJG AKAM ALB ALGN ALK ALL ALLE AMAT "
                 "AMCR AMD AME AMGN AMP AMT AMZN ANET ANSS ANTM AON AOS APA "
                 "APD APH APTV ARE ATO ATVI AVB AVGO AVY AWK AXP AZO BA BAC "
                 "BAX BBWI BBY BDX BEN BF-B BIIB BIO BK BKNG BKR BLK BLL BMY "
                 "BR BRK-B BRO BSX BWA BXP C CAG CAH CARR CAT CB CBOE CBRE "
                 "CCI CCL CDAY CDNS CDW CE CERN CF CFG CHD CHRW CHTR CI CINF "
                 "CL CLX CMA CMCSA CME CMG CMI CMS CNC CNP COF COO COP COST "
                 "CPB CPRT CRL CRM CSCO CSX CTAS CTLT CTRA CTSH CTVA CTXS CVS "
                 "CVX CZR D DAL DD DE DFS DG DGX DHI DHR DIS DISCA DISCK DISH "
                 "DLR DLTR DOV DOW DPZ DRE DRI DTE DUK DVA DVN DXC DXCM EA "
                 "EBAY ECL ED EFX EIX EL EMN EMR ENPH EOG EQIX EQR ES ESS ETN "
                 "ETR ETSY EVRG EW EXC EXPD EXPE EXR F FANG FAST FB FBHS FCX "
                 "FDX FE FFIV FIS FISV FITB FLT FMC FOX FOXA FRC FRT FTNT FTV "
                 "GD GE GILD GIS GL GLW GM GNRC GOOG GOOGL GPC GPN GPS GRMN "
                 "GS GWW HAL HAS HBAN HBI HCA HD HES HIG HII HLT HOLX HON HPE "
                 "HPQ HRL HSIC HST HSY HUM HWM IBM ICE IDXX IEX IFF ILMN INCY "
                 "INFO INTC INTU IP IPG IPGP IQV IR IRM ISRG IT ITW IVZ J "
                 "JBHT JCI JKHY JNJ JNPR JPM K KEY KEYS KHC KIM KLAC KMB KMI "
                 "KMX KO KR KSU L LDOS LEG LEN LH LHX LIN LKQ LLY LMT LNC LNT "
                 "LOW LRCX LUMN LUV LVS LW LYB LYV MA MAA MAR MAS MCD MCHP "
                 "MCK MCO MDLZ MDT MET MGM MHK MKC MKTX MLM MMC MMM MNST MO "
                 "MOS MPC MPWR MRK MRNA MRO MS MSCI MSFT MSI MTB MTCH MTD MU "
                 "NCLH NDAQ NEE NEM NFLX NI NKE NLOK NLSN NOC NOW NRG NSC "
                 "NTAP NTRS NUE NVDA NVR NWL NWS NWSA NXPI O ODFL OGN OKE OMC "
                 "ORCL ORLY OTIS OXY PAYC PAYX PBCT PCAR PEAK PEG PENN PEP "
                 "PFE PFG PG PGR PH PHM PKG PKI PLD PM PNC PNR PNW POOL PPG "
                 "PPL PRU PSA PSX PTC PVH PWR PXD PYPL QCOM QRVO RCL RE REG "
                 "REGN RF RHI RJF RL RMD ROK ROL ROP ROST RSG RTX SBAC SBUX "
                 "SCHW SEE SHW SIVB SJM SLB SNA SNPS SO SPG SPGI SRE STE STT "
                 "STX STZ SWK SWKS SYF SYK SYY T TAP TDG TDY TECH TEL TER TFC "
                 "TFX TGT TJX TMO TMUS TPR TRMB TROW TRV TSCO TSLA TSN TT "
                 "TTWO TWTR TXN TXT TYL UA UAA UAL UDR UHS ULTA UNH UNP UPS "
                 "URI USB V VFC VIAC VLO VMC VNO VRSK VRSN VRTX VTR VTRS VZ "
                 "WAB WAT WBA WDC WEC WELL WFC WHR WLTW WM WMB WMT WRB WRK "
                 "WST WU WY WYNN XEL XLNX XOM XRAY XYL YUM ZBH ZBRA ZION ZTS")

def get_sp500_history(tickers: str = sp500_tickers) -> pandas.DataFrame:
    """
    Returns a Pandas DataFrame with historical data for the S&P 500,
    downloaded from Yahoo Finance. Uses tickers from October 27th 2021,
    which can be overridden if the user so chooses.

    :param tickers: Ticker symbols, default set to S&P 500 companies.
    :type tickers: str
    :return: A Pandas DataFrame with historical data for the S&P 500.
    :rtype: Pandas.DataFrame
    """
    return yfinance.download(tickers)