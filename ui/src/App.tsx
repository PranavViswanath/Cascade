import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Upload, FileText, Brain, Network, Sparkles, CheckCircle, AlertCircle } from 'lucide-react';
import { Paper, CitationCascade, AnalysisResult, InputType } from './types';
import { api } from './services/api';
import LoadingSpinner from './components/LoadingSpinner';
import PaperCard from './components/PaperCard';
import SynthesisCard from './components/SynthesisCard';

const App: React.FC = () => {
  const [inputType, setInputType] = useState<InputType>('text');
  const [claim, setClaim] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [currentStep, setCurrentStep] = useState('');
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleAnalyze = async () => {
    if (!claim.trim()) return;

    setIsAnalyzing(true);
    setError(null);
    setAnalysisResult(null);

    try {
      // Step 1: Detect contradictions
      setCurrentStep('detecting');
      const contradictions = await api.detectContradictions(claim);

      // Step 2: Propagate citations
      setCurrentStep('propagating');
      const citationCascades = await api.propagateCitations(contradictions);

      // Step 3: Generate synthesis
      setCurrentStep('synthesizing');
      const synthesis = await api.generateSynthesis(claim, contradictions, citationCascades);

      setAnalysisResult({
        claim,
        contradictions,
        citationCascades,
        synthesis
      });
    } catch (err) {
      setError('An error occurred during analysis. Please try again.');
    } finally {
      setIsAnalyzing(false);
      setCurrentStep('');
    }
  };

  const getStepMessage = () => {
    switch (currentStep) {
      case 'detecting':
        return 'Searching for contradictory research papers via Perplexity...';
      case 'propagating':
        return 'Mapping citation cascades and impact networks...';
      case 'synthesizing':
        return 'Formulating research strategy with NVIDIA NeMo...';
      default:
        return 'Analyzing research claim...';
    }
  };

  return (
    <div className="min-h-screen gradient-bg">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-12"
        >
          <div className="flex items-center justify-center space-x-3 mb-4">
            <div className="w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-600 rounded-xl flex items-center justify-center">
              <Search className="w-6 h-6 text-white" />
            </div>
            <h1 className="text-4xl font-bold text-gray-900">Research Integrity Network</h1>
          </div>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Find research contradictions, map citation impact, and prioritize what matters—all from either a claim or a paper PDF!
          </p>
        </motion.div>

        {/* Input Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="max-w-4xl mx-auto mb-8"
        >
          <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8">
            {/* Input Type Selection */}
            <div className="mb-6">
              <label className="text-sm font-medium text-gray-700 mb-3 block">How would you like to analyze a research claim?</label>
              <div className="flex space-x-4">
                <button
                  onClick={() => setInputType('text')}
                  className={`flex items-center space-x-2 px-4 py-3 rounded-lg border-2 transition-all ${
                    inputType === 'text'
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <FileText className="w-5 h-5" />
                  <span>Enter a claim</span>
                </button>
                <button
                  onClick={() => setInputType('pdf')}
                  className={`flex items-center space-x-2 px-4 py-3 rounded-lg border-2 transition-all ${
                    inputType === 'pdf'
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <Upload className="w-5 h-5" />
                  <span>Upload a PDF</span>
                </button>
              </div>
            </div>

            {/* Input Field */}
            {inputType === 'text' ? (
              <div className="mb-6">
                <label className="text-sm font-medium text-gray-700 mb-2 block">
                  Enter your research claim
                </label>
                <textarea
                  value={claim}
                  onChange={(e) => setClaim(e.target.value)}
                  placeholder="Example: 'LLMs are not good at reasoning'"
                  className="w-full h-32 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent resize-none"
                />
              </div>
            ) : (
              <div className="mb-6">
                <label className="text-sm font-medium text-gray-700 mb-2 block">
                  Upload your research paper as PDF
                </label>
                <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-primary-400 transition-colors">
                  <Upload className="w-12 h-12 text-gray-400 mx-auto mb-4" />
                  <p className="text-gray-600">Drag and drop your PDF here, or click to browse</p>
                </div>
              </div>
            )}

            {/* Analyze Button */}
            <button
              onClick={handleAnalyze}
              disabled={!claim.trim() || isAnalyzing}
              className="w-full bg-gradient-to-r from-primary-500 to-primary-600 text-white py-4 px-6 rounded-lg font-semibold text-lg hover:from-primary-600 hover:to-primary-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center space-x-2"
            >
              {isAnalyzing ? (
                <>
                  <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                  <span>Analyzing...</span>
                </>
              ) : (
                <>
                  <Search className="w-5 h-5" />
                  <span>🔎 Analyze Research Claim</span>
                </>
              )}
            </button>
          </div>
        </motion.div>

        {/* Loading State */}
        <AnimatePresence>
          {isAnalyzing && (
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.9 }}
              className="max-w-4xl mx-auto mb-8"
            >
              <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8">
                <LoadingSpinner step={currentStep} message={getStepMessage()} />
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Error State */}
        <AnimatePresence>
          {error && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="max-w-4xl mx-auto mb-8"
            >
              <div className="bg-red-50 border border-red-200 rounded-xl p-6">
                <div className="flex items-center space-x-3">
                  <AlertCircle className="w-6 h-6 text-red-500" />
                  <div>
                    <h3 className="text-lg font-semibold text-red-800">Analysis Error</h3>
                    <p className="text-red-600">{error}</p>
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Results */}
        <AnimatePresence>
          {analysisResult && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="max-w-4xl mx-auto space-y-8"
            >
              {/* Contradictions Section */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8"
              >
                <div className="flex items-center space-x-3 mb-6">
                  <div className="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center">
                    <FileText className="w-5 h-5 text-white" />
                  </div>
                  <div>
                    <h2 className="text-2xl font-bold text-gray-900">1️⃣ Relevant Papers Found</h2>
                    <p className="text-gray-600">Contradictory research papers discovered</p>
                  </div>
                </div>

                {analysisResult.contradictions.length > 0 ? (
                  <div className="space-y-4">
                    {analysisResult.contradictions.map((paper, index) => (
                      <PaperCard key={index} paper={paper} index={index} />
                    ))}
                  </div>
                ) : (
                  <div className="text-center py-8">
                    <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
                      <CheckCircle className="w-8 h-8 text-gray-400" />
                    </div>
                    <p className="text-gray-600">No contradictory papers found.</p>
                  </div>
                )}
              </motion.div>

              {/* Citation Cascades Section */}
              {analysisResult.contradictions.length > 0 && (
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8"
                >
                  <div className="flex items-center space-x-3 mb-6">
                    <div className="w-10 h-10 bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg flex items-center justify-center">
                      <Network className="w-5 h-5 text-white" />
                    </div>
                    <div>
                      <h2 className="text-2xl font-bold text-gray-900">2️⃣ Citation Cascades</h2>
                      <p className="text-gray-600">Impact mapping from contradicted papers</p>
                    </div>
                  </div>

                  {Object.keys(analysisResult.citationCascades).length > 0 ? (
                    <div className="space-y-4">
                      {Object.entries(analysisResult.citationCascades).map(([paperTitle, citations], index) => (
                        <motion.div
                          key={index}
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: index * 0.1 }}
                          className="bg-gray-50 rounded-lg p-4"
                        >
                          <h4 className="font-semibold text-gray-900 mb-2">{paperTitle}</h4>
                          <p className="text-sm text-gray-600 mb-2">Cited by:</p>
                          <ul className="space-y-1">
                            {citations.map((citation, idx) => (
                              <li key={idx} className="text-sm text-gray-700 flex items-center space-x-2">
                                <div className="w-1 h-1 bg-primary-500 rounded-full"></div>
                                <span>{citation}</span>
                              </li>
                            ))}
                          </ul>
                        </motion.div>
                      ))}
                    </div>
                  ) : (
                    <div className="text-center py-8">
                      <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
                        <Network className="w-8 h-8 text-gray-400" />
                      </div>
                      <p className="text-gray-600">No citation cascades found.</p>
                    </div>
                  )}
                </motion.div>
              )}

              {/* Synthesis Section */}
              <SynthesisCard synthesis={analysisResult.synthesis} />

              {/* Success Message */}
              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                className="bg-green-50 border border-green-200 rounded-xl p-6 text-center"
              >
                <div className="flex items-center justify-center space-x-3">
                  <CheckCircle className="w-6 h-6 text-green-500" />
                  <span className="text-green-800 font-semibold">Analysis Complete!</span>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
};

export default App;
