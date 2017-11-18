start "Squishserver Window" /B "C:\squish-5.0.0-java-win32\bin\squishserver" --verbose

For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c%%a%%b)
For /f "tokens=1-2 delims=/:" %%a in ("%TIME%") do (set mytime=%%a%%b)


set TIMESTAMP=%mydate%%mytime%

set RESULTFOLDER=C:\squish-results\%TIMESTAMP%\

mkdir %RESULTFOLDER%

set RESULTFILE=%RESULTFOLDER%result.xml
set GTESTRESULTFILE=%RESULTFOLDER%gtestresult.xml
set EMAILIDS=aaa



C:\squish-5.0.0-java-win32\bin\squishrunner --testsuite C:\tooling_auto\suite_CascadesBuilder_sanity --testcase tst_Components_view  ^
																									 --testcase tst_Outline_view ^
																									 --testcase tst_Properties_view ^
																									 --testcase tst_Release ^
																									 --testcase tst_Debug_Qml ^
																									 --testcase tst_Debug_Js ^
																									 --testcase tst_Debug_Native ^
																									 --testcase tst_Debug_PrettyPrinting ^
																									 --testcase tst_Debug_Qtypes ^
																									 --testcase tst_Debug_Redebug ^
																									 --testcase tst_CS4_Profile ^
																									 --testcase tst_CS4_ReProfile ^
																									 --testcase tst_Template_Projects ^
																									 --reportgen xmljunit,%RESULTFILE% --resultdir %RESULTFOLDER%

parse.py  -i %RESULTFILE%  -o %GTESTRESULTFILE% -e %EMAILIDS% -t %TIMESTAMP%

C:\squish-5.0.0-java-win32\bin\squishserver --stop