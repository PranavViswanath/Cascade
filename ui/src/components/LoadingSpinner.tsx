import React from 'react';
import { motion } from 'framer-motion';
import { Search, Brain, Network, Sparkles } from 'lucide-react';

interface LoadingSpinnerProps {
  step: string;
  message: string;
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({ step, message }) => {
  const getIcon = () => {
    switch (step) {
      case 'extracting':
        return <Search className="w-6 h-6" />;
      case 'analyzing-start':
        return <Brain className="w-6 h-6" />;
      case 'deep-search':
        return <Search className="w-6 h-6" />;
      case 'validating-sources':
        return <Sparkles className="w-6 h-6" />;
      case 'citation-mapping':
        return <Network className="w-6 h-6" />;
      case 'impact-analysis':
        return <Network className="w-6 h-6" />;
      case 'synthesis-prep':
        return <Brain className="w-6 h-6" />;
      case 'generating-strategy':
        return <Sparkles className="w-6 h-6" />;
      default:
        return <Sparkles className="w-6 h-6" />;
    }
  };

  const getGradientClass = () => {
    switch (step) {
      case 'extracting':
        return 'from-blue-500 to-purple-600';
      case 'analyzing-start':
        return 'from-purple-500 to-pink-600';
      case 'deep-search':
        return 'from-green-500 to-blue-600';
      case 'validating-sources':
        return 'from-yellow-500 to-orange-600';
      case 'citation-mapping':
        return 'from-indigo-500 to-purple-600';
      case 'impact-analysis':
        return 'from-purple-500 to-red-600';
      case 'synthesis-prep':
        return 'from-pink-500 to-rose-600';
      case 'generating-strategy':
        return 'from-emerald-500 to-teal-600';
      default:
        return 'from-primary-500 to-primary-600';
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="flex flex-col items-center justify-center p-8"
    >
      <motion.div
        animate={{ rotate: 360 }}
        transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
        className="relative w-20 h-20 mb-6"
      >
        <div className="absolute inset-0 rounded-full border-4 border-gray-200"></div>
        <motion.div
          animate={{ rotate: -360 }}
          transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
          className={`absolute inset-0 rounded-full border-4 border-transparent bg-gradient-to-r ${getGradientClass()}`}
          style={{
            borderTopWidth: '4px',
            borderTopStyle: 'solid',
            borderTopColor: 'transparent',
            background: `conic-gradient(from 0deg, transparent, var(--tw-gradient-stops))`
          }}
        />
        <motion.div
          animate={{ scale: [1, 1.1, 1] }}
          transition={{ duration: 2, repeat: Infinity }}
          className={`absolute inset-2 rounded-full bg-gradient-to-br ${getGradientClass()} flex items-center justify-center text-white shadow-lg`}
        >
          {getIcon()}
        </motion.div>
      </motion.div>
      
      <motion.h3
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="text-lg font-semibold text-gray-800 mb-2"
      >
        {message}
      </motion.h3>
      
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4 }}
        className="flex space-x-2"
      >
        {[0, 1, 2, 3].map((i) => (
          <motion.div
            key={i}
            animate={{ 
              y: [0, -12, 0],
              scale: [1, 1.2, 1]
            }}
            transition={{ 
              duration: 0.8, 
              repeat: Infinity, 
              delay: i * 0.15,
              ease: "easeInOut"
            }}
            className={`w-3 h-3 bg-gradient-to-r ${getGradientClass()} rounded-full shadow-md`}
          />
        ))}
      </motion.div>
    </motion.div>
  );
};

export default LoadingSpinner;
