#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Fm Stereo Tx
# Author: Naga
# Generated: Mon Feb 25 16:32:20 2013
##################################################

from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class FM_stereo_tx(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Fm Stereo Tx")

		##################################################
		# Variables
		##################################################
		self.st_gain = st_gain = 10
		self.samp_rate = samp_rate = 195.312e3
		self.pilot_gain = pilot_gain = 80e-3
		self.mpx_rate = mpx_rate = 160e3
		self.Mono_gain = Mono_gain = 300e-3
		self.FM_freq = FM_freq = 96.5e6

		##################################################
		# Blocks
		##################################################
		_st_gain_sizer = wx.BoxSizer(wx.VERTICAL)
		self._st_gain_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_st_gain_sizer,
			value=self.st_gain,
			callback=self.set_st_gain,
			label='st_gain',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._st_gain_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_st_gain_sizer,
			value=self.st_gain,
			callback=self.set_st_gain,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_st_gain_sizer)
		_pilot_gain_sizer = wx.BoxSizer(wx.VERTICAL)
		self._pilot_gain_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_pilot_gain_sizer,
			value=self.pilot_gain,
			callback=self.set_pilot_gain,
			label='pilot_gain',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._pilot_gain_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_pilot_gain_sizer,
			value=self.pilot_gain,
			callback=self.set_pilot_gain,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_pilot_gain_sizer)
		self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "FM")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "audio")
		self.Add(self.notebook_0)
		_Mono_gain_sizer = wx.BoxSizer(wx.VERTICAL)
		self._Mono_gain_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_Mono_gain_sizer,
			value=self.Mono_gain,
			callback=self.set_Mono_gain,
			label='Mono_gain',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._Mono_gain_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_Mono_gain_sizer,
			value=self.Mono_gain,
			callback=self.set_Mono_gain,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_Mono_gain_sizer)
		_FM_freq_sizer = wx.BoxSizer(wx.VERTICAL)
		self._FM_freq_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_FM_freq_sizer,
			value=self.FM_freq,
			callback=self.set_FM_freq,
			label='FM_freq',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._FM_freq_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_FM_freq_sizer,
			value=self.FM_freq,
			callback=self.set_FM_freq,
			minimum=88e6,
			maximum=108e6,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_FM_freq_sizer)
		self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
			self.notebook_0.GetPage(1).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_fftsink2_1.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.notebook_0.GetPage(0).GetWin(),
			baseband_freq=FM_freq,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
		self.uhd_usrp_sink_0 = uhd.usrp_sink(
			device_addr="addr=192.168.10.2",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
		self.uhd_usrp_sink_0.set_center_freq(FM_freq, 0)
		self.uhd_usrp_sink_0.set_gain(0, 0)
		self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
		self.low_pass_filter_0 = gr.fir_filter_fff(1, firdes.low_pass(
			Mono_gain, mpx_rate, 15000, 2000, firdes.WIN_HAMMING, 6.76))
		self.gr_vector_to_streams_0 = gr.vector_to_streams(gr.sizeof_short*1, 2)
		self.gr_sub_xx_0 = gr.sub_ff(1)
		self.gr_sig_source_x_1 = gr.sig_source_f(160000, gr.GR_SIN_WAVE, 19000, pilot_gain, 0)
		self.gr_sig_source_x_0 = gr.sig_source_f(160000, gr.GR_SIN_WAVE, 38000, 30e-3, 0)
		self.gr_short_to_float_1 = gr.short_to_float(1, 1)
		self.gr_short_to_float_0 = gr.short_to_float(1, 1)
		self.gr_multiply_xx_0 = gr.multiply_vff(1)
		self.gr_multiply_const_vxx_2 = gr.multiply_const_vcc((32.768e3, ))
		self.gr_multiply_const_vxx_1 = gr.multiply_const_vff((30e-6, ))
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vff((30e-6, ))
		self.gr_frequency_modulator_fc_0 = gr.frequency_modulator_fc(980e-3)
		self.gr_file_source_0 = gr.file_source(gr.sizeof_short*2, "/home/kranthi/Documents/project/FM Transceiver/FM Transmitter/test.raw", True)
		self.gr_add_xx_1 = gr.add_vff(1)
		self.gr_add_xx_0 = gr.add_vff(1)
		self.blks2_rational_resampler_xxx_2 = blks2.rational_resampler_fff(
			interpolation=4,
			decimation=1,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_rational_resampler_xxx_1 = blks2.rational_resampler_fff(
			interpolation=5,
			decimation=1,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_fff(
			interpolation=5,
			decimation=1,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_fm_preemph_0 = blks2.fm_preemph(fs=mpx_rate, tau=50e-6)
		self.band_pass_filter_0 = gr.fir_filter_fff(1, firdes.band_pass(
			st_gain, mpx_rate, 23000, 53000, 2000, firdes.WIN_HAMMING, 6.76))

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_file_source_0, 0), (self.gr_vector_to_streams_0, 0))
		self.connect((self.gr_vector_to_streams_0, 0), (self.gr_short_to_float_0, 0))
		self.connect((self.gr_vector_to_streams_0, 1), (self.gr_short_to_float_1, 0))
		self.connect((self.gr_short_to_float_0, 0), (self.gr_multiply_const_vxx_0, 0))
		self.connect((self.gr_short_to_float_1, 0), (self.gr_multiply_const_vxx_1, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.gr_multiply_const_vxx_1, 0), (self.blks2_rational_resampler_xxx_1, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.gr_add_xx_0, 1))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.gr_sub_xx_0, 1))
		self.connect((self.blks2_rational_resampler_xxx_1, 0), (self.gr_sub_xx_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_1, 0), (self.gr_add_xx_0, 0))
		self.connect((self.gr_add_xx_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.gr_sig_source_x_0, 0), (self.gr_multiply_xx_0, 0))
		self.connect((self.gr_sub_xx_0, 0), (self.gr_multiply_xx_0, 1))
		self.connect((self.gr_multiply_xx_0, 0), (self.band_pass_filter_0, 0))
		self.connect((self.gr_sig_source_x_1, 0), (self.gr_add_xx_1, 0))
		self.connect((self.band_pass_filter_0, 0), (self.gr_add_xx_1, 1))
		self.connect((self.low_pass_filter_0, 0), (self.gr_add_xx_1, 2))
		self.connect((self.gr_add_xx_1, 0), (self.blks2_fm_preemph_0, 0))
		self.connect((self.blks2_fm_preemph_0, 0), (self.blks2_rational_resampler_xxx_2, 0))
		self.connect((self.blks2_rational_resampler_xxx_2, 0), (self.gr_frequency_modulator_fc_0, 0))
		self.connect((self.gr_frequency_modulator_fc_0, 0), (self.gr_multiply_const_vxx_2, 0))
		self.connect((self.gr_multiply_const_vxx_2, 0), (self.uhd_usrp_sink_0, 0))
		self.connect((self.gr_multiply_const_vxx_2, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.gr_multiply_const_vxx_1, 0), (self.wxgui_fftsink2_1, 0))

	def get_st_gain(self):
		return self.st_gain

	def set_st_gain(self, st_gain):
		self.st_gain = st_gain
		self._st_gain_slider.set_value(self.st_gain)
		self._st_gain_text_box.set_value(self.st_gain)
		self.band_pass_filter_0.set_taps(firdes.band_pass(self.st_gain, self.mpx_rate, 23000, 53000, 2000, firdes.WIN_HAMMING, 6.76))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

	def get_pilot_gain(self):
		return self.pilot_gain

	def set_pilot_gain(self, pilot_gain):
		self.pilot_gain = pilot_gain
		self._pilot_gain_slider.set_value(self.pilot_gain)
		self._pilot_gain_text_box.set_value(self.pilot_gain)
		self.gr_sig_source_x_1.set_amplitude(self.pilot_gain)

	def get_mpx_rate(self):
		return self.mpx_rate

	def set_mpx_rate(self, mpx_rate):
		self.mpx_rate = mpx_rate
		self.band_pass_filter_0.set_taps(firdes.band_pass(self.st_gain, self.mpx_rate, 23000, 53000, 2000, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_0.set_taps(firdes.low_pass(self.Mono_gain, self.mpx_rate, 15000, 2000, firdes.WIN_HAMMING, 6.76))

	def get_Mono_gain(self):
		return self.Mono_gain

	def set_Mono_gain(self, Mono_gain):
		self.Mono_gain = Mono_gain
		self._Mono_gain_slider.set_value(self.Mono_gain)
		self._Mono_gain_text_box.set_value(self.Mono_gain)
		self.low_pass_filter_0.set_taps(firdes.low_pass(self.Mono_gain, self.mpx_rate, 15000, 2000, firdes.WIN_HAMMING, 6.76))

	def get_FM_freq(self):
		return self.FM_freq

	def set_FM_freq(self, FM_freq):
		self.FM_freq = FM_freq
		self._FM_freq_slider.set_value(self.FM_freq)
		self._FM_freq_text_box.set_value(self.FM_freq)
		self.wxgui_fftsink2_0.set_baseband_freq(self.FM_freq)
		self.uhd_usrp_sink_0.set_center_freq(self.FM_freq, 0)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = FM_stereo_tx()
	tb.Run(True)

