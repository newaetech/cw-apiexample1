function [ ciphertext, trace ] = measure_AES( scope, target, plaintext, key )
%MEASURE_AES Perform a single AES measurement.
%   'plaintext' should be input to AES algorithm
%   'key' should be key used in AES algorithm
%   Returns both the ciphertext & the trace data.

import py.cwapi.measure_AES
result = measure_AES(scope, target, plaintext, key);

%Do insane conversion
pyct = result{1,1};
pyctCELL = cell(pyct);
ciphertext = cellfun(@uint8, pyctCELL);

%Do insane conversion
pywave = result{1,2};
pywaveCELL = cell(pywave);
trace = cellfun(@double, pywaveCELL);

end

