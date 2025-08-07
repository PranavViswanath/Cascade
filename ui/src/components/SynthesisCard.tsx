import React from 'react';
import { motion } from 'framer-motion';
import { Lightbulb, TrendingUp, Target } from 'lucide-react';

interface SynthesisCardProps {
  synthesis: string;
}

const SynthesisCard: React.FC<SynthesisCardProps> = ({ synthesis }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-gradient-to-br from-primary-50 to-white rounded-xl shadow-lg border border-primary-100 p-6"
    >
      <div className="flex items-center space-x-3 mb-4">
        <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-600 rounded-lg flex items-center justify-center">
          <Lightbulb className="w-5 h-5 text-white" />
        </div>
        <div>
          <h3 className="text-lg font-semibold text-gray-900">Research Strategy</h3>
          <p className="text-sm text-gray-600">AI-powered recommendations</p>
        </div>
      </div>
      
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="prose prose-sm max-w-none"
      >
        <div className="bg-white rounded-lg p-4 border border-gray-200">
          <p className="text-gray-700 leading-relaxed whitespace-pre-wrap">
            {synthesis}
          </p>
        </div>
      </motion.div>
      
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4 }}
        className="mt-4 flex items-center justify-between"
      >
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-1 text-xs text-gray-500">
            <TrendingUp className="w-3 h-3" />
            <span>AI Analysis</span>
          </div>
          <div className="flex items-center space-x-1 text-xs text-gray-500">
            <Target className="w-3 h-3" />
            <span>Strategic Focus</span>
          </div>
        </div>
        
        <div className="flex space-x-2">
          <button className="px-3 py-1 text-xs bg-primary-100 text-primary-700 rounded-full hover:bg-primary-200 transition-colors">
            Copy
          </button>
          <button className="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition-colors">
            Export
          </button>
        </div>
      </motion.div>
    </motion.div>
  );
};

export default SynthesisCard;
