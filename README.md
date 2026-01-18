# FluxCapFilter

Low pass filter for capacitive flow rate.


Next steps
- [ ] apply filter to Cap Time Series
- [ ] Output clean time series csv file
  - Columns: time, capacitance (filtered),       capacitance unfiltered
- [ ] plot filtered and unfiltered time series on subplot.


# Spec
## apply filter 
add method to model class get_filtered_capdata()
takes cap_data applies filter tp it returns filtered data

## output clean time series
write_clean_time_series_csv()
inputs 
- time
- filtered capdata
- unfiltered capdata 

return
- null

write filename like ("path/jc.yyyy-mm-dd.hh-mm-ss.csv")
writes csv file of filtered and unfiltered time series

## plot both time series
