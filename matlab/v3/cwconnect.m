function [ cwapi ] = cwconnect( offset, totalsamples )
%CWCONNECT Connect to a ChipWhisperer-Lite, return the object.
%   Connects to a ChipWhisperer-Lite. You must have already configured
%   python for this to work & have a WORKING ChipWhisperer install.s

if nargin < 2
  totalsamples = 3000;
end
if nargin < 1
  offset = 1250;
end

import py.cwapi.cwconnect

cwapi = cwconnect(offset, totalsamples);


end

