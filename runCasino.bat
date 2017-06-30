for /F "tokens=1,2,3 delims=-" %%a in ("%date%") do (set mydate=%%a%%b%%c)
for /F "tokens=1-2 delims=/:" %%a in ("%TIME%") do (set mytime=%%a%%b)


set TIMESTAMP=%mydate%_%mytime%

set SANITY_DIR=\\10.33.0.158\AutomationDesk\CasinoGuiTest_New\SikuliX\CasinoSanityTest.sikuli

set EMAIL_IDS=qiangx,leonli

REM set CLIENT_DIR=D:\QA_Builds\PokerStars.UK
set CLIENT_DIR=D:\QA_Builds\PokerStars.com_2016-11-02_08-38-23_QA_FlashBuild-master_311

java -jar D:\CasinoGuiTest_New\SikuliX\SikuliTool\sikulix.jar -r %SANITY_DIR% --args %TIMESTAMP%

python \\10.33.0.158\AutomationDesk\CasinoGuiTest_New\SikuliX\TestBases\reportSent.py %CLIENT_DIR% %TIMESTAMP%


