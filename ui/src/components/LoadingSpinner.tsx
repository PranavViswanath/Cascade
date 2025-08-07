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
      case 'detecting':
        return <Search className="w-6 h-6" />;
      case 'propagating':
        return <Network className="w-6 h-6" />;
      case 'synthesizing':
        return <Brain className="w-6 h-6" />;
      default:
        return <Sparkles className="w-6 h-6" />;
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
        className="relative w-16 h-16 mb-4"
      >
        <div className="absolute inset-0 rounded-full border-4 border-primary-200"></div>
        <motion.div
          animate={{ rotate: -360 }}
          transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
          className="absolute inset-0 rounded-full border-4 border-transparent border-t-primary-500"
        />
        <div className="absolute inset-0 flex items-center justify-center">
          {getIcon()}
        </div>
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
        className="flex space-x-1"
      >
        {[0, 1, 2].map((i) => (
          <motion.div
            key={i}
            animate={{ y: [0, -10, 0] }}
            transition={{ duration: 0.6, repeat: Infinity, delay: i * 0.2 }}
            className="w-2 h-2 bg-primary-500 rounded-full"
          />
        ))}
      </motion.div>
    </motion.div>
  );
};

export default LoadingSpinner;
