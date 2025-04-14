const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/:login*', // Ajustar según backend real
      },
    ];
  },
};

export default nextConfig;
