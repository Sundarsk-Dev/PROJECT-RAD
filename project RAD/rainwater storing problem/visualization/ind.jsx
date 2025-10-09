import React, { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw, SkipForward } from 'lucide-react';

const RainwaterVisualizer = () => {
  const presetExamples = [
    { name: "Classic", heights: [0,1,0,2,1,0,1,3,2,1,2,1], expected: 6 },
    { name: "Simple Valley", heights: [4,2,0,3,2,5], expected: 9 },
    { name: "Tiny Valley", heights: [3,0,3], expected: 3 },
    { name: "Multiple Peaks", heights: [4,2,3], expected: 1 },
    { name: "No Trap", heights: [5,4,3,2,1], expected: 0 }
  ];

  const [heights, setHeights] = useState(presetExamples[0].heights);
  const [left, setLeft] = useState(0);
  const [right, setRight] = useState(heights.length - 1);
  const [leftMax, setLeftMax] = useState(0);
  const [rightMax, setRightMax] = useState(0);
  const [totalWater, setTotalWater] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [stepLog, setStepLog] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);

  const maxHeight = Math.max(...heights, 1);
  const barWidth = Math.min(60, 600 / heights.length);

  useEffect(() => {
    if (isPlaying && left < right) {
      const timer = setTimeout(step, 800);
      return () => clearTimeout(timer);
    } else if (left >= right) {
      setIsPlaying(false);
    }
  }, [isPlaying, left, right]);

  const reset = () => {
    setLeft(0);
    setRight(heights.length - 1);
    setLeftMax(0);
    setRightMax(0);
    setTotalWater(0);
    setIsPlaying(false);
    setStepLog([]);
    setCurrentStep(0);
  };

  const step = () => {
    if (left >= right) return;

    let newLeft = left;
    let newRight = right;
    let newLeftMax = leftMax;
    let newRightMax = rightMax;
    let newTotalWater = totalWater;
    let logMessage = "";

    if (heights[left] < heights[right]) {
      if (heights[left] >= leftMax) {
        newLeftMax = heights[left];
        logMessage = `Step ${currentStep + 1}: Left wall updated! height[${left}]=${heights[left]} becomes new left_max. No water trapped (at a wall).`;
      } else {
        const water = leftMax - heights[left];
        newTotalWater += water;
        logMessage = `Step ${currentStep + 1}: Trapped ${water} units at position ${left}. Water level = left_max(${leftMax}) - height(${heights[left]}) = ${water}. Total water: ${newTotalWater}`;
      }
      newLeft = left + 1;
    } else {
      if (heights[right] >= rightMax) {
        newRightMax = heights[right];
        logMessage = `Step ${currentStep + 1}: Right wall updated! height[${right}]=${heights[right]} becomes new right_max. No water trapped (at a wall).`;
      } else {
        const water = rightMax - heights[right];
        newTotalWater += water;
        logMessage = `Step ${currentStep + 1}: Trapped ${water} units at position ${right}. Water level = right_max(${rightMax}) - height(${heights[right]}) = ${water}. Total water: ${newTotalWater}`;
      }
      newRight = right - 1;
    }

    setLeft(newLeft);
    setRight(newRight);
    setLeftMax(newLeftMax);
    setRightMax(newRightMax);
    setTotalWater(newTotalWater);
    setStepLog(prev => [...prev, logMessage]);
    setCurrentStep(prev => prev + 1);
  };

  const loadPreset = (preset) => {
    setHeights(preset.heights);
    reset();
  };

  const getWaterHeight = (index) => {
    if (index < 0 || index >= heights.length) return 0;
    if (index > left && index < right) {
      const effectiveLeftMax = index >= left ? leftMax : 0;
      const effectiveRightMax = index <= right ? rightMax : 0;
      const waterLevel = Math.min(effectiveLeftMax, effectiveRightMax);
      return Math.max(0, waterLevel - heights[index]);
    }
    if (index <= left) {
      return Math.max(0, leftMax - heights[index]);
    }
    if (index >= right) {
      return Math.max(0, rightMax - heights[index]);
    }
    return 0;
  };

  return (
    <div className="w-full max-w-5xl mx-auto p-6 bg-gradient-to-br from-blue-50 to-cyan-50 rounded-xl shadow-lg">
      <h1 className="text-3xl font-bold text-center mb-2 text-gray-800">
        Trapping Rainwater - Two Pointer Algorithm
      </h1>
      <p className="text-center text-gray-600 mb-6">
        Watch how the algorithm finds trapped water between elevation bars
      </p>

      {/* Presets */}
      <div className="mb-6 flex flex-wrap gap-2 justify-center">
        {presetExamples.map((preset, idx) => (
          <button
            key={idx}
            onClick={() => loadPreset(preset)}
            className="px-4 py-2 bg-white border-2 border-blue-300 rounded-lg hover:bg-blue-100 transition text-sm font-medium"
          >
            {preset.name} ({preset.expected} units)
          </button>
        ))}
      </div>

      {/* Visualization */}
      <div className="bg-white p-6 rounded-lg shadow-md mb-6">
        <div className="flex justify-center items-end h-80 gap-1 mb-4">
          {heights.map((h, i) => {
            const water = getWaterHeight(i);
            const isLeftPointer = i === left;
            const isRightPointer = i === right;
            const isPastLeft = i < left;
            const isPastRight = i > right;
            
            return (
              <div
                key={i}
                className="relative flex flex-col justify-end"
                style={{ width: `${barWidth}px` }}
              >
                {/* Water */}
                {water > 0 && (
                  <div
                    className="w-full bg-blue-400 opacity-60"
                    style={{ height: `${(water / maxHeight) * 250}px` }}
                  />
                )}
                {/* Bar */}
                <div
                  className={`w-full transition-all ${
                    isLeftPointer ? 'bg-green-500' :
                    isRightPointer ? 'bg-red-500' :
                    isPastLeft || isPastRight ? 'bg-gray-300' :
                    'bg-gray-700'
                  }`}
                  style={{ height: `${(h / maxHeight) * 250}px` }}
                />
                {/* Pointer Labels */}
                {isLeftPointer && (
                  <div className="absolute -bottom-8 left-1/2 transform -translate-x-1/2 text-green-600 font-bold text-xs whitespace-nowrap">
                    L ({h})
                  </div>
                )}
                {isRightPointer && (
                  <div className="absolute -bottom-8 left-1/2 transform -translate-x-1/2 text-red-600 font-bold text-xs whitespace-nowrap">
                    R ({h})
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* Legend */}
        <div className="flex justify-center gap-6 text-sm mb-4">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-green-500"></div>
            <span>Left Pointer</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-red-500"></div>
            <span>Right Pointer</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-blue-400 opacity-60"></div>
            <span>Trapped Water</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-gray-700"></div>
            <span>Elevation Bar</span>
          </div>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
        <div className="bg-white p-4 rounded-lg shadow text-center">
          <div className="text-sm text-gray-600">Left Max</div>
          <div className="text-2xl font-bold text-green-600">{leftMax}</div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow text-center">
          <div className="text-sm text-gray-600">Right Max</div>
          <div className="text-2xl font-bold text-red-600">{rightMax}</div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow text-center">
          <div className="text-sm text-gray-600">Current Step</div>
          <div className="text-2xl font-bold text-gray-700">{currentStep}</div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow text-center">
          <div className="text-sm text-gray-600">Total Water</div>
          <div className="text-2xl font-bold text-blue-600">{totalWater}</div>
        </div>
      </div>

      {/* Controls */}
      <div className="flex justify-center gap-4 mb-6">
        <button
          onClick={() => setIsPlaying(!isPlaying)}
          disabled={left >= right}
          className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center gap-2 font-medium"
        >
          {isPlaying ? <Pause size={20} /> : <Play size={20} />}
          {isPlaying ? 'Pause' : 'Play'}
        </button>
        <button
          onClick={step}
          disabled={left >= right || isPlaying}
          className="px-6 py-3 bg-green-500 text-white rounded-lg hover:bg-green-600 disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center gap-2 font-medium"
        >
          <SkipForward size={20} />
          Step
        </button>
        <button
          onClick={reset}
          className="px-6 py-3 bg-gray-500 text-white rounded-lg hover:bg-gray-600 flex items-center gap-2 font-medium"
        >
          <RotateCcw size={20} />
          Reset
        </button>
      </div>

      {/* Step Log */}
      <div className="bg-white p-4 rounded-lg shadow max-h-48 overflow-y-auto">
        <h3 className="font-bold mb-2 text-gray-800">Algorithm Steps:</h3>
        {stepLog.length === 0 ? (
          <p className="text-gray-500 text-sm">Click "Step" or "Play" to start the algorithm</p>
        ) : (
          <div className="space-y-1">
            {stepLog.map((log, idx) => (
              <div key={idx} className="text-sm text-gray-700 border-l-2 border-blue-300 pl-3 py-1">
                {log}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default RainwaterVisualizer;