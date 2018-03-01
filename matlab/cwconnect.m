function [ cwapi, scope, target ] = cwconnect( offset, totalsamples )
%CWCONNECT Connect to a ChipWhisperer-Lite, return the object.
%   Connects to a ChipWhisperer-Lite. You must have already configured
%   python for this to work & have a WORKING ChipWhisperer install.s

if nargin < 2
  totalsamples = 3000;
end
if nargin < 1
  offset = 1250;
end

cwapi = py.importlib.import_module('cwapi');

result = cwapi.cwconnect(offset, totalsamples);

cwapi = result{1,1};
scope = result{1,2};
target = result{1,3};
end

